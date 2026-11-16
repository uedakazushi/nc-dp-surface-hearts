#!/usr/bin/env python3
"""Exact six-point reconstruction for the cubic idempotent corner.

Uses only Python's standard library.  Verifies six universal polynomial identities
in nine independent p_ij variables, the finite-geometry criterion over F7,
and exact rational examples.  Uses no Groebner rank or experimental AS-regularity
claim: sufficiency uses AOU's rolled-up helix theorem and Serre vanishing.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
import json

NV = 12
ONE = {(0,) * NV: 1}
ZERO = {}

def variable(i):
    e = [0] * NV; e[i] = 1
    return {tuple(e): 1}

def add(a, b):
    c = dict(a)
    for mon, coeff in b.items():
        c[mon] = c.get(mon, 0) + coeff
        if not c[mon]: del c[mon]
    return c

def neg(a): return {m: -v for m, v in a.items()}

def sub(a, b): return add(a, neg(b))

def mul(a, b):
    d = defaultdict(int)
    for m, u in a.items():
        for n, v in b.items():
            d[tuple(i + j for i, j in zip(m, n))] += u * v
    return {m: v for m, v in d.items() if v}

def dot(a, b):
    z = ZERO
    for x, y in zip(a, b): z = add(z, mul(x, y))
    return z

def cross(a, b):
    return [sub(mul(a[1], b[2]), mul(a[2], b[1])),
            sub(mul(a[2], b[0]), mul(a[0], b[2])),
            sub(mul(a[0], b[1]), mul(a[1], b[0]))]

# p_i have 9 algebraically independent coordinates, X has 3.
p = [[variable(3 * i + c) for c in range(3)] for i in range(3)]
X = [variable(9 + i) for i in range(3)]
E = [[ONE if i == j else ZERO for i in range(3)] for j in range(3)]
U = [[mul(v[0], v[1]), mul(v[1], v[2]), mul(v[2], v[0])] for v in p]
mon2 = [mul(X[0], X[1]), mul(X[1], X[2]), mul(X[2], X[0])]
conic = [dot(cross(U[(i + 1) % 3], U[(i + 2) % 3]), mon2) for i in range(3)]
other_line = [dot(cross(p[(i + 1) % 3], p[(i + 2) % 3]), X) for i in range(3)]
identities = []
for c in range(3):
    lines = [dot(cross(p[i], E[c]), X) for i in range(3)]
    f = ZERO; g = ZERO
    for i in range(3):
        f = add(f, mul(p[i][c], mul(conic[i], lines[i])))
        g = add(g, mul(other_line[i], lines[i]))
    identities += [not f, not g]
assert len(identities) == 6 and all(identities)


def det3(A):
    return (A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
            - A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
            + A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0]))

def all_2x2(A):
    return [A[i][c] * A[j][d] - A[i][d] * A[j][c]
            for i, j in combinations(range(3), 2)
            for c, d in combinations(range(3), 2)]

def Q_good(q):
    assert all(x for row in q for x in row)
    return all(all_2x2(q)) and det3(q) != 0 and det3([[1/x for x in row] for row in q]) != 0

def six_general(q):
    # P=(entrywise reciprocal Q)^t: three moving columns + coordinate triangle.
    P = [[1/q[b][c] for b in range(3)] for c in range(3)]
    entries = all(x for row in P for x in row)
    one_coordinate_two_moving = all(all_2x2(P))
    moving_three = det3(P) != 0
    conic = [[P[0][i] * P[1][i], P[1][i] * P[2][i], P[2][i] * P[0][i]] for i in range(3)]
    no_six_conic = det3(conic) != 0
    return entries and one_coordinate_two_moving and moving_three and no_six_conic

q_witness = [[F(1), F(1), F(1)], [F(1), F(-1,4), F(1,16)], [F(1), F(1,6), F(-1,4)]]
q_bad_det = [[F(n) for n in row] for row in ((3,4,5),(5,6,7),(7,8,9))]
q_bad_recip = [[F(2520)/x for x in row] for row in q_bad_det]
for q, expected in ((q_witness,True),(q_bad_det,False),(q_bad_recip,False)):
    assert Q_good(q) == six_general(q) == expected

# Independent exhaustive comparison of two equivalent conditions over F7.
p = 7
def inv7(x): return pow(x,-1,p)
def det7(A): return det3(A) % p
def good7(q):
    minor = all(x % p for x in all_2x2(q))
    return minor and det7(q)!=0 and det7([[inv7(x) for x in row] for row in q])!=0

def points7(q):
    P = [[inv7(q[b][c]) for b in range(3)] for c in range(3)]
    conic = [[P[0][i]*P[1][i],P[1][i]*P[2][i],P[2][i]*P[0][i]] for i in range(3)]
    return all(x % p for x in all_2x2(P)) and det7(P)!=0 and det7(conic)!=0

count = 0
for a,b,c,d in product(range(1,p),repeat=4):
    q = [[1,1,1],[1,a,b],[1,c,d]]
    assert good7(q) == points7(q)
    count += good7(q)
assert count == 80

result = {
    'date': '2026-11-15', 'version': 'corner-v4/geometric-reconstruction-v1',
    'universal_integer_polynomial_identities': 6,
    'geometric_relations': 'w1_bc = P_cb, w2_bc = 1',
    'reconstruction': 'P=(entrywise_inverse(Q))^transpose',
    'rational_cases': 3, 'F7_cross_ratio_points': 6**4,
    'F7_general_position_points': count,
    'F7_equivalence_11_versus_six_general': True,
    'scope': 'Finite algebra equivalence uses AOU rolled-up helix (4.9) and Serre vanishing; this code checks elementary universal polynomial identities and sample geometry, not AS-regularity of arbitrary potentials.'
}
output = Path('build/cubic_corner_six_points_certificate.json')
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 6 universal polynomial identities; 3 rational cases; F7 1296 points with 80 general configurations.')
