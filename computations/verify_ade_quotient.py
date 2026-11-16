#!/usr/bin/env python3
"""Exact low-rank checks for the ADE quotient and the isolated-root example.

Rational relation spaces, not numerical theta evaluation. Does not prove the
enhanced-category lemma, formality, sheaf existence, or novelty.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def paths(adj, degree):
    pp = [(i,) for i in range(len(adj))]
    for _ in range(degree):
        pp = [p + (j,) for p in pp for j in adj[p[-1]]]
    return pp


def quotient(adj, degree, start, end):
    pp = [p for p in paths(adj, degree) if p[0] == start and p[-1] == end]
    index = {p: i for i, p in enumerate(pp)}
    rows = []
    # Every homogeneous relation is a path times a vertex relation times a path.
    for left_degree in range(degree - 1):
        for left in paths(adj, left_degree):
            if left[0] != start:
                continue
            for right in paths(adj, degree - 2 - left_degree):
                if right[0] != left[-1] or right[-1] != end:
                    continue
                i = left[-1]
                row = [0] * len(pp)
                for j in adj[i]:
                    path = left + (j,) + right
                    row[index[path]] += 1 if i < j else -1
                rows.append(row)
    rank = sp.Matrix(rows).rank() if rows and pp else 0
    return len(pp) - rank


def cartan_and_hilbert(adj, cutoff):
    n = len(adj)
    matrices = [sp.Matrix(n, n, lambda i, j: quotient(adj, d, i, j))
                for d in range(cutoff + 1)]
    assert matrices[-1] == sp.zeros(n)
    # The relations are homogeneous and the algebra is generated in degree 1;
    # vanishing at cutoff therefore implies vanishing in every larger degree.
    return sum(matrices, sp.zeros(n)), [sum(m) for m in matrices]


def main():
    c2, h2 = cartan_and_hilbert([[1], [0]], 2)
    c3, h3 = cartan_and_hilbert([[1], [0, 2], [1]], 3)
    assert h2 == [2, 2, 0]
    assert h3 == [3, 4, 3, 0]
    assert c3 == sp.Matrix([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    m = sp.Matrix([1, 2, 3])
    assert (m.T * c3 * m)[0] == 40
    # Non-scalar A3 representation: central return paths need not vanish
    # separately. Their signed sum vanishes, while each has rank one.
    col, row = sp.Matrix([1, 0]), sp.Matrix([[0, 1]])
    assert row * col == sp.zeros(1)
    assert col * row == sp.Matrix([[0, 1], [0, 0]])
    assert col * row - col * row == sp.zeros(2)
    # Specialization of the known Dynkin matrix Hilbert formula (Etingof--Rains,
    # math/0503393v3, Section 1, (1)); not a relation-space computation in E6.
    adjacency = sp.zeros(6)
    for i, j in [(0, 3), (1, 2), (2, 3), (3, 4), (4, 5)]:
        adjacency[i, j] = adjacency[j, i] = 1
    hh = [sp.eye(6), adjacency]
    for _ in range(2, 12):
        hh.append(adjacency*hh[-1] - hh[-2])
    assert hh[-1] == sp.zeros(6)
    c6 = sum(hh, sp.zeros(6))
    assert sum(c6) == 156
    m6 = sp.Matrix([6, 1, 1, 2, 2, 4])
    assert (m6.T*c6*m6)[0] == 970
    nakayama = [0, 5, 4, 3, 2, 1]
    perm = sp.zeros(6)
    for i, j in enumerate(nakayama):
        perm[i, j] = 1
    assert hh[10] == perm
    assert (m6.T*m6)[0] == 62
    assert (m6.T*perm*m6)[0] == 52
    assert [int((m6.T*h*m6)[0]) for h in hh] == [
        62, 54, 73, 120, 125, 102, 135, 126, 73, 48, 52, 0]
    nn = sp.symbols('n1:7')
    mm = sp.Matrix([sum(nn[:3])] + [nn[i+1]-nn[i] for i in range(5)])
    dimension_formula = sum(nn)**2 + sum((nn[5-i]-nn[i])**2 for i in range(3))
    assert sp.expand((mm.T*c6*mm)[0] - dimension_formula) == 0
    frobenius_constraints = [mm[1]-mm[5], mm[2]-mm[4]]
    paired_sums = [nn[0]+nn[5]-nn[1]-nn[4],
                   nn[1]+nn[4]-nn[2]-nn[3]]
    assert all(sp.expand(a+b) == 0
               for a, b in zip(frobenius_constraints, paired_sums))
    # Symmetric six-point sums give a positive example of the criterion.
    symmetric_m = mm.subs(dict(zip(nn, range(1, 7))))
    assert perm*symmetric_m == symmetric_m
    assert (symmetric_m.T*c6*symmetric_m)[0] == 476

    # Coordinates in the independent generators (q,x,y,z,w,v) of E.
    pp = [sp.Matrix(a) for a in [
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0),
        (-1, -1, -1, 0, 0, 0), (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)]]
    roots = []
    for a in range(-2, 3):
        for b in product(range(-2, 3), repeat=6):
            if sum(b) == 3*a and sum(x*x for x in b) - a*a == 2:
                roots.append((a, b))
    # This bound exhausts E6: Cauchy--Schwarz gives |a| <= 2;
    # sum b_i(b_i-1)=(a-1)(a-2), together with the sum, bounds b_i.
    assert len(roots) == 72
    resonant = []
    for a, b in roots:
        rho = -sum((bi*pi for bi, pi in zip(b, pp)), sp.zeros(6, 1))
        if all(rho[i] == 0 for i in range(1, 6)):
            resonant.append((a, b, -int(rho[0])))
    assert sorted(r[-1] for r in resonant) == [-1, 1]
    assert {r[0] for r in resonant} == {-1, 1}
    q = sp.Matrix([1, 0, 0, 0, 0, 0])
    ysum = sum(pp[3:], sp.zeros(6, 1))
    shifts = [-2*q, -ysum, sp.zeros(6, 1)]
    assert all(pp[c] - pp[b] + t != sp.zeros(6, 1)
               for c in range(3, 6) for b in range(3) for t in shifts)
    result = dict(A2_hilbert=h2, A3_hilbert=h3, A3_cartan=c3.tolist(),
                  weighted_A3_quotient_dimension=40, E6_roots=len(roots),
                  E6_cartan=c6.tolist(), E6_basic_dimension=156,
                  weighted_E6_quotient_dimension=970,
                  E6_nakayama=nakayama, E6_semisimple_quotient_dimension=62,
                  E6_right_socle_dimension=52, E6_example_is_Frobenius=False,
                  symmetric_six_point_quotient_dimension=476,
                  symmetric_six_point_is_Frobenius=True,
                  symbolic_sorted_six_point_dimension_formula=str(dimension_formula),
                  isolated_resonant_roots=resonant, nonzero_theta_arguments=27,
                  scope="Exact finite checks only; categorical proofs are in the paper.")
    dest = Path('build/ade_quotient_checks.json')
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(result, indent=2, default=int) + '\n')
    print('PASS: A2/A3 relations, weighted quotient dimension, isolated E6 root, 27 theta arguments')


if __name__ == '__main__':
    main()
