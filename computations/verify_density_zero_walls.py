#!/usr/bin/env python3
"""Exact finite checks for maximal resonance and the two zero-wall examples.

The proofs of Zariski density, dg-kernel equality, and categorical statements
are in the manuscript. These finite computations do not prove those results.
Requires Python 3 and SymPy (the repository's requirements.txt).
"""
from __future__ import annotations

import itertools
import json
import random
from collections import deque
from typing import Iterable

import sympy as sp

Vector = tuple[int, ...]


def pairing(a: Vector, b: Vector) -> int:
    return a[0] * b[0] - sum(x * y for x, y in zip(a[1:], b[1:]))


def simple_roots(r: int) -> list[Vector]:
    result = [(1, 1, 1, 1) + (0,) * (r - 3)]
    for i in range(r - 1):
        v = [0] * (r + 1)
        v[i + 1], v[i + 2] = -1, 1
        result.append(tuple(v))
    return result


def roots_by_reflection(r: int) -> set[Vector]:
    simples = simple_roots(r)
    roots = set(simples)
    queue = deque(simples)
    while queue:
        v = queue.popleft()
        for alpha in simples:
            k = pairing(v, alpha)
            w = tuple(x + k * y for x, y in zip(v, alpha))
            if w not in roots:
                roots.add(w)
                queue.append(w)
    return roots


def roots_by_classes(r: int) -> set[Vector]:
    positive: set[Vector] = set()
    for i in range(r):
        for j in range(i + 1, r):
            b = [0] * r
            b[i], b[j] = -1, 1
            positive.add((0, *b))
    for degree, count in ((1, 3), (2, 6)):
        for chosen in itertools.combinations(range(r), count):
            b = [int(i in chosen) for i in range(r)]
            positive.add((degree, *b))
    if r == 8:
        for i in range(r):
            b = [1] * r
            b[i] = 2
            positive.add((3, *b))
    return positive | {tuple(-x for x in v) for v in positive}


def linear_combination(coefficients: Iterable[int], vectors: list[Vector]) -> Vector:
    coefficients = tuple(coefficients)
    return tuple(sum(c * v[j] for c, v in zip(coefficients, vectors))
                 for j in range(len(vectors[0])))


def add(*vectors: Vector) -> Vector:
    return tuple(sum(values) for values in zip(*vectors))


def neg(v: Vector) -> Vector:
    return tuple(-x for x in v)


def verify() -> dict[str, object]:
    rng = random.Random(20261117)
    counts = {3: 8, 4: 20, 5: 40, 6: 72, 7: 126, 8: 240}
    tested_lists = 0
    for r, count in counts.items():
        roots = roots_by_reflection(r)
        assert roots == roots_by_classes(r)
        assert len(roots) == count
        assert all(pairing(v, v) == -2 and sum(v[1:]) == 3 * v[0] for v in roots)
        for _ in range(40):
            ns = rng.sample(range(1, 201), r)
            assert all(sum(b * n for b, n in zip(v[1:], ns)) != 0 for v in roots)
            tested_lists += 1
        # The point-to-simple-index matrix has determinant of absolute value 3.
        index_matrix = sp.zeros(r)
        index_matrix[0, 0:3] = sp.ones(1, 3)
        for i in range(1, r):
            index_matrix[i, i - 1], index_matrix[i, i] = -1, 1
        assert abs(index_matrix.det()) == 3
        # Cumulative sums and any coordinate permutation are unimodular.
        cumulative = sp.Matrix([[int(j <= i) for j in range(r)] for i in range(r)])
        assert cumulative.det() == 1
        for _ in range(12):
            order = rng.sample(range(r), r)
            matrix = sp.zeros(r)
            for j, i in enumerate(order):
                matrix[i, :] = cumulative[j, :]
            assert abs(matrix.det()) == 1

    # Coefficients in the Q-linearly independent basis q,x,y,z,w,v.
    basis = [tuple(int(i == j) for j in range(6)) for i in range(6)]
    q, x, y, z, w, v = basis
    zero = (0,) * 6
    points = [x, y, neg(add(x, y)), z, w, v]
    roots = roots_by_reflection(6)
    resonance = []
    for root in roots:
        value = linear_combination(root[1:], points)
        if value[1:] == (0,) * 5:
            resonance.append((root, value[0]))
    assert len(resonance) == 2 and {m for _, m in resonance} == {0}
    collinear = [indices for indices in itertools.combinations(range(6), 3)
                 if add(*(points[i] for i in indices)) == zero]
    assert collinear == [(0, 1, 2)]
    assert add(*points) != zero
    Y = add(z, w, v)
    u, t = neg(q), neg(Y)
    assert u != zero and t != zero and add(u, neg(t)) != zero
    theta_arguments = [add(points[3 + c], neg(points[b]), shift)
                       for shift in (u, t, zero) for b in range(3) for c in range(3)]
    assert len(theta_arguments) == 27 and all(a != zero for a in theta_arguments)

    Q = sp.Matrix([[1, 1, 1], [1, 2, 2], [1, 3, 4]])
    reciprocal = Q.applyfunc(lambda a: 1 / a)
    zero_minors = [(rows, columns)
                   for rows in itertools.combinations(range(3), 2)
                   for columns in itertools.combinations(range(3), 2)
                   if Q.extract(rows, columns).det() == 0]
    assert zero_minors == [((0, 1), (1, 2))]
    assert Q.det() == 1 and reciprocal.det() == sp.Rational(1, 24)
    six = [(1, 1, 1), (2, 1, 1), (12, 4, 3), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    X, Yc, Z = sp.symbols('x y z')
    a, b, c, d = sp.symbols('A B C D')
    sections = [sp.Rational(1, 3)*X**2*(Yc-Z)-X*Yc*(Yc-Z),
                sp.Rational(7, 12)*X**2*(Yc-Z)-X*(Yc**2-Z**2),
                sp.Rational(1, 6)*X**2*(Yc+2*Z)-sp.Rational(3, 2)*X*Yc**2+Yc**2*Z,
                sp.Rational(1, 4)*X**2*(Yc+Z)-sp.Rational(3, 2)*X*Yc**2+Yc*Z**2]
    assert all(section.subs(dict(zip((X, Yc, Z), point))) == 0
               for section in sections for point in six)
    equation = (23*a**3-22*a**2*b+44*a**2*c-42*a**2*d+8*a*b**2-16*a*b*c
                -24*a*c**2+24*a*d**2+8*b**2*c+24*b*c**2-24*b*c*d)
    assert sp.expand(equation.subs(dict(zip((a, b, c, d), sections)), simultaneous=True)) == 0
    node = {a: 0, b: 0, c: 1, d: 1}
    assert all(sp.diff(equation, variable).subs(node) == 0 for variable in (a, b, c, d))
    hessian = sp.hessian(equation.subs(c, 1), (a, b, d)).subs(node).det()
    assert hessian == -2304
    return {
        'status': 'PASS', 'root_counts': counts, 'positive_integer_lists': tested_lists,
        'simple_index_determinant_absolute': 3,
        'order_matrix_tests': 72,
        'elliptic_zero_wall_resonant_roots': sorted(resonance),
        'elliptic_zero_wall_collinear_triples_one_based': [[1, 2, 3]],
        'elliptic_zero_wall_nonzero_theta_linear_forms': len(theta_arguments),
        'rational_wall_zero_minor': zero_minors,
        'rational_wall_determinants': [1, '1/24'],
        'cubic_polynomial_identity': True, 'node_hessian_determinant': int(hessian),
        'scope': 'Exact finite arithmetic; no computational proof of density, existence of sheaves, or dg equivalence.'
    }


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
