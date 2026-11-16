#!/usr/bin/env python3
"""Integer checks of the sorted cyclic-point spectrum (hearts-v21).

Reuses the independent Cartan/Weyl enumeration in verify_four_hearts_chambers.
Checks all 720 orderings for the displayed cubic multiset and sampled orders
in degrees 1 through 6. These are lattice checks, not proofs of Rains sheaf
existence or of equality of t-structures; the primary-source inputs and
categorical arguments are stated in the manuscript.
"""
from __future__ import annotations
import argparse
from itertools import combinations, permutations
import json
from pathlib import Path
from random import Random
from verify_four_hearts_chambers import roots, run_algorithm, value


def picard_basis(order: tuple[int, ...]) -> list[tuple[int, ...]]:
    """D=a*h-sum(b_i*e_i) in the fixed labels 0,...,r-1."""
    r = len(order)
    a0 = [1] + [int(i in order[:3]) for i in range(r)]
    result = [tuple(a0)]
    for i, j in zip(order, order[1:]):
        a = [0] * (r + 1)
        a[i + 1], a[j + 1] = -1, 1
        result.append(tuple(a))
    return result


def combine(coeff: tuple[int, ...], basis: list[tuple[int, ...]]) -> tuple[int, ...]:
    return tuple(sum(c * row[j] for c, row in zip(coeff, basis))
                 for j in range(len(basis[0])))


def direct_positive_roots(r: int) -> set[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    for i, j in combinations(range(r), 2):
        a = [0] * (r + 1); a[i + 1], a[j + 1] = -1, 1
        out.add(tuple(a))
    for degree, count in ((1, 3), (2, 6)):
        for sub in combinations(range(r), count):
            out.add((degree,) + tuple(int(i in sub) for i in range(r)))
    if r == 8:
        for j in range(r):
            out.add((3,) + tuple(2 if i == j else 1 for i in range(r)))
    return out


def check_order(ns: tuple[int, ...], rr: set[tuple[int, ...]], edges: list[tuple[int, int]]) -> dict:
    if min(ns) < 1 or len(set(ns)) != len(ns):
        raise ValueError('The theorem requires distinct positive integers.')
    r = len(ns)
    basis = picard_basis(tuple(range(r)))
    m = (sum(ns[:3]),) + tuple(b - a for a, b in zip(ns, ns[1:]))
    positive = {x for x in rr if all(c >= 0 for c in x)}
    assert {combine(x, basis) for x in positive} == direct_positive_roots(r)
    for x in rr:
        d = combine(x, basis)
        assert d[0] ** 2 - sum(b * b for b in d[1:]) == -2
        assert 3 * d[0] - sum(d[1:]) == 0
        assert value(m, x) == sum(b * n for b, n in zip(d[1:], ns)) != 0
    inversions = sum(ns[i] > ns[j] for i in range(r) for j in range(i + 1, r))
    assert sum(value(m, x) < 0 for x in positive) == inversions
    seq, terminal, dimensions = run_algorithm(m, edges, rr, 0)
    assert 0 not in seq
    assert len(seq) == inversions
    order = tuple(sorted(range(r), key=ns.__getitem__))
    assert [combine(x, basis) for x in terminal] == picard_basis(order)
    nu = tuple(sorted(ns))
    expected = [sum(nu[:3])] + [b - a for a, b in zip(nu, nu[1:])]
    assert dimensions == expected
    assert (not seq) == (ns == nu)
    assert sum(d == 1 for d in dimensions) == sum(b - a == 1 for a, b in zip(nu, nu[1:]))
    return {'indices': list(m), 'inversions': inversions, 'sequence': seq, 'dimensions': dimensions}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('build/four_hearts_sorted_checks.json'))
    parser.add_argument('--samples', type=int, default=40)
    args = parser.parse_args()
    if args.samples < 1:
        raise ValueError('--samples must be positive')
    rng = Random(20261116)
    counts = {3: 8, 4: 20, 5: 40, 6: 72, 7: 126, 8: 240}
    results = []
    for r in range(3, 9):
        edges = ([(0, 3)] if r >= 4 else []) + [(i, i + 1) for i in range(1, r - 1)]
        rr = roots(r, edges)
        assert len(rr) == counts[r]
        for _ in range(args.samples):
            check_order(tuple(rng.sample(range(1, 91), r)), rr, edges)
        results.append({'rank': r, 'degree': 9 - r, 'root_count': len(rr), 'sampled_orders': args.samples})
        if r == 6:
            rr6, edges6 = rr, edges
    displayed = check_order((1, 3, 2, 5, 7, 11), rr6, edges6)
    canonical = (1, 2, 3, 5, 7, 11)
    histogram: dict[int, int] = {}
    simple_bases: set[frozenset[tuple[int, ...]]] = set()
    for p in permutations(range(6)):
        check = check_order(tuple(canonical[i] for i in p), rr6, edges6)
        histogram[check['inversions']] = histogram.get(check['inversions'], 0) + 1
        simple_bases.add(frozenset(picard_basis(p)))
    assert len(simple_bases) == 720 and sum(histogram.values()) == 720
    assert histogram[0] == histogram[15] == 1
    assert all(histogram[i] == histogram[15 - i] for i in histogram)
    expected_histogram = [1, 5, 14, 29, 49, 71, 90, 101, 101, 90, 71, 49, 29, 14, 5, 1]
    assert [histogram[i] for i in range(16)] == expected_histogram
    out = {
        'date': '2026-11-16', 'version': 'hearts-v21', 'arithmetic': 'exact integers',
        'degree_1_to_6_sampling': results, 'random_orders': 6 * args.samples,
        'all_cubic_permutations': 720, 'distinct_cubic_simple_root_bases': 720,
        'cubic_inversion_histogram': expected_histogram, 'displayed_E6_example': displayed,
        'root_enumeration_cross_checked_against_Picard_list': True,
        'geometric_existence_proved_by_computation': False,
        'categorical_heart_equality_proved_by_computation': False,
        'scope': 'The exact lattice/sorting statements only; Rains existence and derived comparison are separate mathematical inputs.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
