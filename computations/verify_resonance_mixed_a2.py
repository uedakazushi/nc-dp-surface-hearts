#!/usr/bin/env python3
"""Exact arithmetic for mixed A2 ranks, both tilt chambers, and Pi(A2).

This verifies finite linear algebra, not sheaf existence or derived equivalence.
Actual elliptic generator characters and off-diagonal coefficients are not computed.
Run from the repository root; Python standard library only.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def rank(rows: list[list[int | F]]) -> int:
    if not rows:
        return 0
    a = [[F(x) for x in row] for row in rows]
    cols, pivot = len(a[0]), 0
    if any(len(row) != cols for row in a):
        raise ValueError('Nonrectangular matrix')
    for col in range(cols):
        j = next((j for j in range(pivot, len(a)) if a[j][col]), None)
        if j is None:
            continue
        a[pivot], a[j] = a[j], a[pivot]
        c = a[pivot][col]
        a[pivot] = [x/c for x in a[pivot]]
        for j in range(len(a)):
            if j != pivot and a[j][col]:
                c = a[j][col]
                a[j] = [x-c*y for x,y in zip(a[j],a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


# Vertex dimensions, scalar x:+->-, scalar y:-->+.
REPS = {'S+': (1,0,0,0), 'S-': (0,1,0,0),
        'P': (1,1,1,0), 'Q': (1,1,0,1)}


def hom_dim(src: tuple[int,...], dst: tuple[int,...]) -> int:
    a,b,x,y = src
    c,d,u,v = dst
    variables = [(0,i,j) for i in range(c) for j in range(a)]
    variables += [(1,i,j) for i in range(d) for j in range(b)]
    index = {key:i for i,key in enumerate(variables)}
    eqs = []
    for side,outdim,indim,middle,targetmid,arr,tar in (
        (1,d,a,b,c,x,u), (0,c,b,a,d,y,v)):
        for i in range(outdim):
            for j in range(indim):
                row = [0]*len(variables)
                for k in range(middle):
                    row[index[(side,i,k)]] += arr
                for k in range(targetmid):
                    row[index[(1-side,k,j)]] -= tar
                eqs.append(row)
    return len(variables)-rank(eqs)


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def flat(a: list[list[int]]) -> list[int]:
    return [x for row in a for x in row]


def unit(i: int, j: int, n: int = 4) -> list[list[int]]:
    return [[int(r == i and c == j) for c in range(n)] for r in range(n)]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def commutant_dim(gens: list[list[list[int]]]) -> int:
    n = len(gens[0]); basis = [unit(i,j,n) for i in range(n) for j in range(n)]
    equations = []
    for g in gens:
        cols = []
        for e in basis:
            eg,ge = multiply(e,g),multiply(g,e)
            cols.append([x-y for x,y in zip(flat(eg),flat(ge))])
        equations.extend(transpose(cols))
    return n*n-rank(equations)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,
        default=Path('build/resonance_mixed_a2_certificate.json'))
    args = parser.parse_args()
    names = list(REPS)
    hom = [[hom_dim(REPS[u],REPS[v]) for v in names] for u in names]
    assert hom == [[1,0,0,1],[0,1,1,0],[1,0,1,1],[0,1,1,1]]
    dims = [(1,0),(0,1),(1,1),(1,1)]
    euler = [[2*a*c+2*b*d-a*d-b*c for c,d in dims] for a,b in dims]
    ext1 = [[hom[i][j]+hom[j][i]-euler[i][j] for j in range(4)]
            for i in range(4)]
    assert ext1 == [[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]
    counts = {'positive_sum':0,'negative_sum':0,'balanced_sum':0}
    for p,n in product(range(1,9),repeat=2):
        r = min(p,n)
        if p>n:
            assert (3-2*(p-n) == 1) == (p-n == 1)
        for aa,bb,cc,dd in product(range(5),repeat=4):
            a,b,t = aa+cc+dd,bb+cc+dd,cc
            h0 = p*aa+max(p-n,0)*cc+p*dd
            h1 = n*bb+max(n-p,0)*cc+n*dd
            assert (h0,h1) == (p*a-r*t,n*b-r*t)
            assert h0-h1 == p*a-n*b
            if p>n:
                assert (h1 == 0) == (bb == dd == 0)
                assert (h0 == 0) == (aa == cc == dd == 0)
                counts['positive_sum'] += 1
            elif p<n:
                assert (h1 == 0) == (bb == cc == dd == 0)
                assert (h0 == 0) == (aa == dd == 0)
                counts['negative_sum'] += 1
            else:
                assert (h0 == h1 == 0) == (aa == bb == dd == 0)
                counts['balanced_sum'] += 1
            if p != n:
                assert (h0 == h1 == 0) == (aa+bb+cc+dd == 0)
    # Canonical right-action matrices on the two nonsplit modules V and V'.
    eW = add(unit(0,0),unit(2,2)); eU = add(unit(1,1),unit(3,3))
    a,b = unit(1,0),unit(2,3)
    zero = [[0]*4 for _ in range(4)]
    gens = [eW,eU,a,b]
    assert rank([flat(g) for g in gens]) == 4
    assert multiply(eW,eW)==eW and multiply(eU,eU)==eU
    assert multiply(eW,eU)==multiply(eU,eW)==zero
    assert multiply(eU,a)==multiply(a,eW)==a
    assert multiply(eW,b)==multiply(b,eU)==b
    for x,y in product([a,b],repeat=2):
        assert multiply(x,y) == zero
    for offset in [0,2]:
        blocks = [flat([row[offset:offset+2] for row in g[offset:offset+2]])
                  for g in gens]
        assert rank(blocks)==3
    assert commutant_dim(gens)==4
    cartan = [[-2,1],[1,-2]]
    reflection = [[1,0],[1,-1]]  # columns alpha+beta and -beta
    assert multiply(multiply(transpose(reflection),cartan),reflection)==cartan
    assert multiply([[2,-1]],reflection)==[[1,1]]
    target_order = ['W','U','V','Vprime']
    target_reps = [REPS['S+'],REPS['S-'],REPS['Q'],REPS['P']]
    target_hom = [[hom_dim(u,v) for v in target_reps] for u in target_reps]
    cert = {
        'date':'2026-11-16','version':'resonance-hearts-v8',
        'field':'QQ','source_object_order':names,'source_Hom':hom,
        'source_ambient_Ext1':ext1,'general_indices_range':[1,8],
        'direct_sum_cases':counts,'total_cases':sum(counts.values()),
        'quotient_basis':dict(zip(['eW','eU','a','b'],gens)),
        'quotient_dimension':4,'radical_square_zero':True,
        'both_two_dimensional_image_dimensions':[3,3],
        'regular_module_commutant_dimension':4,
        'Weyl_reflection_matrix':reflection,'reflected_indices':[1,1],
        'target_object_order':target_order,'target_Hom':target_hom,
        'proof_sections':['resonance_mixed_a2_category.tex','resonance_global_heart.tex'],
        'actual_elliptic_generator_matrices_computed':False,
        'sheaf_existence_or_derived_comparison_proved_by_computation':False,
        'scope':'Exact finite linear algebra only. See manuscripts for categorical proofs.'
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(cert,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
