#!/usr/bin/env python3
"""Exact elliptic relation and corner-coordinate checks, hearts-v24.

Construct actual sections using Miller rational functions on a nonsingular
Weierstrass curve over F_1009. Verify all quadratic relations in the function
field (not just at sampled points), then compare the reciprocal coefficient
matrix with the actual degree-three embedding. Special fixtures force each
kind of incidence wall. Standard library only; no analytic theta evaluation.
These finite checks do not prove the complex-geometric theorem or noetherianity.
"""
from __future__ import annotations
import argparse
from itertools import combinations, permutations
import json
from pathlib import Path
from random import Random
from typing import TypeAlias

Point: TypeAlias = tuple[int, int] | None
Poly: TypeAlias = tuple[int, ...]
Elem: TypeAlias = tuple[Poly, Poly]  # a(x)+b(x)y, y^2=x^3-x+1
Rat: TypeAlias = tuple[Elem, Poly]  # denominator in F_p[x]
P = 1009
A, B = -1, 1
ONE: Poly = (1,)
ZERO: Poly = ()
CUBIC: Poly = (B % P, A % P, 0, 1)
RONE: Rat = ((ONE, ZERO), ONE)


def trim(v) -> Poly:
    a = [x % P for x in v]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def pa(a: Poly, b: Poly) -> Poly:
    return trim((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b))))


def pm(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return ZERO
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def ps(c: int, a: Poly) -> Poly:
    return trim(c*x for x in a)


def pe(a: Poly, x: int) -> int:
    val = 0
    for v in reversed(a):
        val = (val*x+v) % P
    return val


def em(a: Elem, b: Elem) -> Elem:
    return pa(pm(a[0], b[0]), pm(pm(a[1], b[1]), CUBIC)), pa(pm(a[0], b[1]), pm(a[1], b[0]))


def rm(a: Rat, b: Rat) -> Rat:
    return em(a[0], b[0]), pm(a[1], b[1])


def re(a: Rat, z: Point) -> int:
    if z is None:
        raise ValueError('Use a finite evaluation point')
    x, y = z
    den = pe(a[1], x)
    if not den:
        raise ValueError('Evaluation at a pole in this presentation')
    return (pe(a[0][0], x) + pe(a[0][1], x)*y) * pow(den, -1, P) % P


def rzero_sum(weights: list[int], fs: list[Rat]) -> bool:
    """Cross-multiply exactly in F_p[x,y]/(y^2-x^3+x-1)."""
    total: Elem = (ZERO, ZERO)
    for i, (w, f) in enumerate(zip(weights, fs)):
        den = ONE
        for j, other in enumerate(fs):
            if i != j:
                den = pm(den, other[1])
        total = (pa(total[0], ps(w, pm(f[0][0], den))),
                 pa(total[1], ps(w, pm(f[0][1], den))))
    return total == (ZERO, ZERO)


def add(p: Point, q: Point) -> Point:
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u and (y+v) % P == 0:
        return None
    slope = ((3*x*x+A)*pow(2*y, -1, P) if p == q else (v-y)*pow((u-x) % P, -1, P)) % P
    z = (slope*slope-x-u) % P
    return z, (slope*(x-z)-y) % P


def neg(p: Point) -> Point:
    return None if p is None else (p[0], -p[1] % P)


def sub(p: Point, q: Point) -> Point:
    return add(p, neg(q))


def summ(points) -> Point:
    out = None
    for p in points:
        out = add(out, p)
    return out


def miller(p: Point, q: Point) -> Rat:
    """div(g_pq)=(p)+(q)-(p+q)-(O), including tangent/vertical cases."""
    if p is None or q is None:
        return RONE
    x, y = p
    u, v = q
    if x == u and (y+v) % P == 0:
        return ((trim((-x, 1)), ZERO), ONE)
    slope = ((3*x*x+A)*pow(2*y, -1, P) if p == q else (v-y)*pow((u-x) % P, -1, P)) % P
    pq = add(p, q)
    assert pq is not None
    return ((trim((slope*x-y, -slope)), ONE), trim((-pq[0], 1)))


def cross(a, b):
    return [(a[(i+1) % 3]*b[(i+2) % 3]-a[(i+2) % 3]*b[(i+1) % 3]) % P for i in range(3)]


def det(m):
    n = len(m)
    ans = 0
    for pi in permutations(range(n)):
        term = (-1)**sum(pi[i] > pi[j] for i in range(n) for j in range(i+1, n))
        for i in range(n):
            term *= m[i][pi[i]]
        ans += term
    return ans % P


def normalize(m):
    if not all(m[0]) or not all(row[0] for row in m):
        raise ValueError('Zero entry on normalization row or column')
    return [[m[i][j]*m[0][0]*pow(m[i][0]*m[0][j] % P, -1, P) % P
             for j in range(3)] for i in range(3)]


def sections_and_relations(points, l0, l1, curve_points):
    sx, sy = summ(points[:3]), summ(points[3:])
    avec = [None, sub(sub(add(sx, sy), l0), l1), sub(sx, l0)]
    cvec = [sub(l0, y) for y in points[3:]]
    w = [[[0]*3 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for c in range(3):
            fs = [rm(miller(sub(x, avec[a]), avec[a]), miller(sub(cvec[c], x), x))
                  for x in points[:3]]
            first = None
            for z in curve_points:
                try:
                    row = [re(f, z) for f in fs]
                except ValueError:
                    continue
                if first is None:
                    if any(row):
                        first = row
                    continue
                weights = cross(first, row)
                if any(weights):
                    break
            else:
                raise AssertionError('Three product sections must span dimension two')
            assert rzero_sum(weights, fs), 'Not an identity in the function field'
            for b in range(3):
                w[a][b][c] = weights[b]
    # Coefficient zeros checked against the complete line-bundle equalities.
    for b in range(3):
        for c in range(3):
            assert (w[0][b][c] == 0) == (l0 == add(sub(sx, points[b]), points[3+c]))
            assert (w[1][b][c] == 0) == (l1 == add(points[b], sub(sy, points[3+c])))
            assert w[2][b][c] != 0
    return w


def projective_matrix(points, l1):
    rows = []
    for c in range(3):
        d, e = [points[3+j] for j in range(3) if j != c]
        third_zero = sub(l1, add(d, e))
        f = rm(miller(d, e), miller(add(d, e), third_zero))
        rows.append([re(f, x) for x in points[:3]])
        assert re(f, points[3+c]) != 0
    return rows


def generic_fixture(points, l0, l1, curve_points):
    if summ(points[3:]) == l1:
        raise ValueError('Last three points are collinear')
    sx, sy = summ(points[:3]), summ(points[3:])
    if l0 == sx or add(l0, l1) == add(sx, sy):
        raise ValueError('Not in the normalized admissible open')
    w = sections_and_relations(points, l0, l1, curve_points)
    pmat = projective_matrix(points, l1)
    # Entry-zero correspondence holds even on mixed 1+2 walls.
    for b in range(3):
        for c in range(3):
            assert (pmat[c][b] == 0) == (w[1][b][c] == 0)
    if any(w[1][b][c] == 0 for b in range(3) for c in range(3)):
        return {'coefficient_wall': True, 'W': w, 'Pmatrix': pmat}
    q = [[w[2][b][c]*pow(w[1][b][c], -1, P) % P for c in range(3)] for b in range(3)]
    reciprocal = [[pow(q[b][c], -1, P) for b in range(3)] for c in range(3)]
    assert normalize(pmat) == normalize(reciprocal)
    minors = []
    for b, bp in combinations(range(3), 2):
        for c, cp in combinations(range(3), 2):
            v = (q[b][c]*q[bp][cp]-q[b][cp]*q[bp][c]) % P
            last = next(j for j in range(3) if j not in (c, cp))
            assert (v == 0) == (l1 == summ((points[b], points[bp], points[3+last])))
            minors.append(v)
    assert (det(reciprocal) == 0) == (l1 == sx)
    assert (det(q) == 0) == (add(l1, l1) == add(sx, sy))
    return {'coefficient_wall': False, 'Q': q, 'Pmatrix': pmat,
            'normalized_P': normalize(pmat), 'minors': minors,
            'det_Q': det(q), 'det_reciprocal': det(reciprocal), 'W': w}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/four_hearts_elliptic_checks.json'))
    args = parser.parse_args()
    assert (4*A**3+27*B**2) % P != 0
    square_roots = {}
    for y in range(P):
        square_roots.setdefault(y*y % P, []).append(y)
    curve_points = [(x, y) for x in range(P) for y in square_roots.get((x**3+A*x+B) % P, [])]
    rng = Random(20261116)
    successes, attempts, relations = 0, 0, 0
    example = None
    while successes < 24:
        attempts += 1
        if attempts > 1000:
            raise RuntimeError('Could not produce enough regular fixtures')
        pts = rng.sample(curve_points, 6)
        l1 = rng.choice(curve_points)
        if any(summ(pts[i] for i in tri) == l1 for tri in combinations(range(6), 3)):
            continue
        if add(l1, l1) == summ(pts):
            continue
        l0s = rng.sample(curve_points, 3)
        try:
            results = [generic_fixture(pts, l0, l1, curve_points) for l0 in l0s]
        except ValueError:
            continue
        assert all(not r['coefficient_wall'] for r in results)
        assert results[0]['normalized_P'] == results[1]['normalized_P'] == results[2]['normalized_P']
        relations += 27
        successes += 1
        if example is None:
            example = {'points': pts, 'L0_Abel': l0s[0], 'L1_Abel': l1,
                       'Q': results[0]['Q'], 'P': results[0]['Pmatrix'],
                       'normalized_reciprocal_Q_transpose': results[0]['normalized_P'],
                       'nine_minors': results[0]['minors'],
                       'det_Q': results[0]['det_Q'], 'det_reciprocal': results[0]['det_reciprocal']}
    wall_tests = {}
    for mode in ('mixed_1plus2', 'mixed_2plus1', 'first_three', 'conic'):
        for attempt in range(1000):
            l1 = rng.choice(curve_points)
            if mode == 'conic':
                pts = rng.sample(curve_points, 5)
                pts.append(sub(add(l1, l1), summ(pts)))
                if pts[-1] is None or len(set(pts)) != 6:
                    continue
            else:
                pts = rng.sample(curve_points, 6)
                indices = {'mixed_1plus2': (0, 3, 4), 'mixed_2plus1': (0, 1, 3), 'first_three': (0, 1, 2)}[mode]
                l1 = summ(pts[i] for i in indices)
            l0 = rng.choice(curve_points)
            try:
                result = generic_fixture(pts, l0, l1, curve_points)
            except ValueError:
                continue
            if mode == 'mixed_1plus2':
                assert result['coefficient_wall'] and result['W'][1][0][2] == 0
            else:
                if result['coefficient_wall']:
                    continue
                if mode == 'mixed_2plus1':
                    assert any(x == 0 for x in result['minors'])
                elif mode == 'first_three':
                    assert result['det_reciprocal'] == 0
                else:
                    assert result['det_Q'] == 0
            wall_tests[mode] = {'points': pts, 'L0_Abel': l0, 'L1_Abel': l1,
                                'predicted_wall_verified': True}
            relations += 9
            break
        else:
            raise RuntimeError(f'Could not test wall {mode}')
    output = {
        'date': '2026-11-16', 'version': 'hearts-v24',
        'curve': {'field_prime': P, 'equation': 'y^2=x^3-x+1', 'number_of_rational_points': len(curve_points)+1},
        'arithmetic': 'F_p[x,y]/(y^2-x^3+x-1), exact rational functions with cross multiplication',
        'regular_six_point_configurations': successes,
        'L0_values_per_configuration': 3,
        'completed_function_field_relation_checks': relations,
        'all_27_coefficient_zero_conditions_checked': True,
        'L0_independence_checked': True,
        'actual_projective_embedding_gauge_comparison': True,
        'regular_example': example,
        'forced_wall_fixtures': wall_tests,
        'complex_geometry_noetherianity_or_heart_equivalence_proved_by_code': False,
        'scope': 'Finite exact checks only; the all-parameter theta/divisor proof is in four_hearts_elliptic_coefficients.tex.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
