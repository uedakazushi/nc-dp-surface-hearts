#!/usr/bin/env python3
"""Exact K0 checks for AOU (4.1); not a proof of heart equivalence.
Run from the repository root with Python 3. No external input is needed.
"""
from fractions import Fraction as Q
from itertools import combinations
import json


def dot(a, b):
    return a[0] * b[0] - sum(x * y for x, y in zip(a[1:], b[1:]))


def transpose(a):
    return [list(row) for row in zip(*a)]


def product(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(a):
    n = len(a)
    m = [[Q(x) for x in row] + [Q(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if m[i][j]), None)
        if pivot is None:
            raise ValueError("Singular matrix")
        m[j], m[pivot] = m[pivot], m[j]
        d = m[j][j]
        m[j] = [x / d for x in m[j]]
        for i in range(n):
            if i != j:
                d = m[i][j]
                m[i] = [x - d * y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def ch_line(d):
    return [Q(1)] + [Q(x) for x in d] + [Q(dot(d, d), 2)]


def twist(v, h):
    r, c, s = v[0], v[1:8], v[8]
    return [r] + [x + r * y for x, y in zip(c, h)] + [s + dot(c, h) + r * Q(dot(h, h), 2)]


def rr(d, e, h):
    f = [y - x for x, y in zip(d, e)]
    return Q(1) + Q(dot(f, f) + dot(f, h), 2)


def main():
    h = [3] + [-1] * 6
    basis = [[0] * 7, [-2] + [1] * 6, [-1, 1, 1, 1, 0, 0, 0]]
    for i in range(1, 4):
        d = [0] * 7
        d[i] = 1
        basis.append(d)
    for i in range(4, 7):
        d = [1] + [0] * 6
        d[i] = -1
        basis.append(d)
    c = [[rr(d, e, h) for e in basis] for d in basis]
    expected = [[Q(i == j) if i // 3 == j // 3 else Q(j // 3 - i // 3) if i < j else Q(0)
                 for j in range(9)] for i in range(9)]
    assert c == expected
    assert sum(map(sum, c)) == 45
    assert dot(h, h) == 3
    chars = transpose([ch_line(d) for d in basis])
    tau = product(inverse(chars), transpose([twist(ch_line(d), h) for d in basis]))
    serre = product(inverse(c), transpose(c))
    assert tau == inverse(serre)
    roots = set()
    for i in range(1, 7):
        for j in range(1, 7):
            if i != j:
                d = [0] * 7
                d[i], d[j] = 1, -1
                roots.add(tuple(d))
    for inds in combinations(range(1, 7), 3):
        d = [1] + [0] * 6
        for i in inds:
            d[i] = -1
        roots.add(tuple(d))
        roots.add(tuple(-x for x in d))
    d = (2, -1, -1, -1, -1, -1, -1)
    roots.add(d)
    roots.add(tuple(-x for x in d))
    assert len(roots) == 72
    assert all(dot(a, a) == -2 and dot(a, h) == 0 for a in roots)
    hs = []
    for n in range(9):
        actual = rr([0] * 7, [n * x for x in h], h)
        assert actual == 1 + Q(3 * n * (n + 1), 2)
        hs.append(int(actual))
    assert all(x.denominator == 1 for row in tau for x in row)
    print(json.dumps({
        "status": "passed", "arithmetic": "rational, exact", "source": "AOU arXiv:2404.00175v1 (4.1)",
        "euler_matrix": [[int(x) for x in row] for row in c],
        "total_euler_dimension": 45, "helix_foundation_length": 9,
        "anticanonical_square": 3, "antiserre_matches_twist": True,
        "antiserre_matrix": [[int(x) for x in row] for row in tau],
        "root_count": 72, "anticanonical_euler_values_n_0_to_8": hs,
        "limitations": "Checks K0 and Euler identities only; not effectivity, AS regularity, t-exactness or faithfulness."
    }, indent=2))


if __name__ == "__main__":
    main()
