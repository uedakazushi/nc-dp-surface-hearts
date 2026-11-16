#!/usr/bin/env python3
"""Exact checks for the explicit cubic corner locus, hearts-v19.

Standard library only. Universal determinant identities are checked over Z
with nine point coordinates and three polynomial variables. Finite corner
checks enumerate ALL quadratic-ideal rows, not sampled relations. No claim
of AS regularity, noetherianity, or categorical existence follows from these
finite calculations; the manuscript supplies the geometric argument.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

PRIME = 1000003
W = [[[1,1,1],[-1,-2,-2],[1,3,1]],
     [[2,1,1],[-1,2,-4],[-1,-3,1]],
     [[1,1,2],[-1,-1,-1],[1,1,1]]]


def det(a):
    n=len(a)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               * prod(a[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def prod(xs):
    ans=1
    for x in xs: ans*=x
    return ans


def checks_q(q):
    minors=[q[i][j]*q[k][l]-q[i][l]*q[k][j]
            for i,k in combinations(range(3),2) for j,l in combinations(range(3),2)]
    return minors+[det(q),det([[1/x for x in row] for row in q])]


# Sparse polynomial ring Z[p_00,...,p_22,X_0,X_1,X_2].
def var(i):
    e=[0]*12; e[i]=1
    return {tuple(e):1}


def plus(*terms):
    out=defaultdict(int)
    for a in terms:
        for m,c in a.items(): out[m]+=c
    return {m:c for m,c in out.items() if c}


def neg(a): return {m:-c for m,c in a.items()}


def times(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():out[tuple(x+y for x,y in zip(u,v))]+=c*d
    return {m:c for m,c in out.items() if c}


def cross(a,b):
    return [plus(times(a[(i+1)%3],b[(i+2)%3]),neg(times(a[(i+2)%3],b[(i+1)%3]))) for i in range(3)]


def dot(a,b): return plus(*(times(x,y) for x,y in zip(a,b)))


def universal_syzygies():
    one={(0,)*12:1}; zero={}
    points=[[var(3*b+c) for c in range(3)] for b in range(3)]
    X=[var(9+c) for c in range(3)]
    mono=[times(X[0],X[1]),times(X[1],X[2]),times(X[2],X[0])]
    u=[[times(p[0],p[1]),times(p[1],p[2]),times(p[2],p[0])] for p in points]
    conics=[dot(cross(u[(b+1)%3],u[(b+2)%3]),mono) for b in range(3)]
    lines=[dot(cross(points[(b+1)%3],points[(b+2)%3]),X) for b in range(3)]
    for c in range(3):
        ec=[one if j==c else zero for j in range(3)]
        L=[dot(cross(p,ec),X) for p in points]
        assert not plus(*(times(times(points[b][c],conics[b]),L[b]) for b in range(3)))
        assert not plus(*(times(lines[b],L[b]) for b in range(3)))
    return 6


def quotient_dimensions(w, modulus=None):
    # Chronological paths; multiplication in the manuscript is opposite order.
    arrows=[(a,b+3) for a,b in product(range(3),repeat=2)]
    arrows += [(b+3,c+6) for b,c in product(range(3),repeat=2)]
    arrows += [(c+6,a) for c,a in product(range(3),repeat=2)]
    rel=defaultdict(dict)
    for a,b,c in product(range(3),repeat=3):
        cycle=(3*a+b,9+3*b+c,18+3*c+a)
        for j,key in enumerate(cycle):
            path=(cycle[(j+1)%3],cycle[(j+2)%3])
            if all(0 not in arrows[k] for k in path):rel[key][path]=w[a][b][c]
    rel=[r for r in rel.values() if r]
    outgoing=defaultdict(list)
    for i,(a,b) in enumerate(arrows):
        if 0 not in (a,b):outgoing[a].append(i)
    assert len(rel)==21 and sum(map(len,outgoing.values()))==21
    paths={0:{(v,v):[()] for v in range(1,9)}}
    out=[8,21]; block_cert=[]
    for n in range(1,8):
        ps=defaultdict(list)
        for (s,t),pp in paths[n-1].items():
            for p in pp:
                for a in outgoing[t]: ps[s,arrows[a][1]].append(p+(a,))
        paths[n]=dict(ps)
        if n==1:continue
        idx={st:{p:j for j,p in enumerate(pp)} for st,pp in ps.items()}
        pivots={st:{} for st in ps}
        for left in range(n-1):
            right=n-2-left
            for relation in rel:
                sample=next(iter(relation)); rs=arrows[sample[0]][0]; rt=arrows[sample[1]][1]
                for (s,t),prefixes in paths[left].items():
                    if t!=rs:continue
                    for (u,v),suffixes in paths[right].items():
                        if u!=rt:continue
                        st=(s,v); table=idx[st]; basis=pivots[st]
                        for pre in prefixes:
                            for suf in suffixes:
                                if len(basis)==len(table):break
                                row={table[pre+p+suf]:(F(z) if modulus is None else z%modulus)
                                     for p,z in relation.items() if z}
                                while row:
                                    j=min(row); coeff=row[j]
                                    if j not in basis:
                                        inv=1/coeff if modulus is None else pow(coeff,-1,modulus)
                                        basis[j]={k:(z*inv if modulus is None else z*inv%modulus) for k,z in row.items()}
                                        break
                                    for k,z in basis[j].items():
                                        value=row.get(k,0)-coeff*z
                                        if modulus is not None:value%=modulus
                                        if value:row[k]=value
                                        else:row.pop(k,None)
        out.append(sum(len(idx[st])-len(pivots[st]) for st in ps))
        if n==7:
            block_cert=[{'endpoints':list(st),'columns':len(idx[st]),'rank':len(pivots[st])} for st in sorted(ps)]
    assert out==[8,21,33,38,33,21,8,0],out
    assert sum(b['columns'] for b in block_cert)==6804
    return out,block_cert


def rank_two_relations():
    # q_bc = (1,2b+1) dot (c+2,1).
    u=[[1,2*b+1] for b in range(3)]
    v=[[c+2,1] for c in range(3)]
    q=[[sum(x*y for x,y in zip(a,b)) for b in v] for a in u]
    h=[1,-2,1]; k=[1,-2,1]
    y=[[h[b]*k[c] for c in range(3)] for b in range(3)]
    assert all(sum(h[b]*u[b][i] for b in range(3))==0 for i in range(2))
    assert all(sum(v[c][i]*k[c] for c in range(3))==0 for i in range(2))
    for b in range(3):
        assert sum(q[b][c]*y[b][c] for c in range(3))==0
        for i in range(2): assert sum(v[c][i]*y[b][c] for c in range(3))==0
    for c in range(3):
        assert sum(q[b][c]*y[b][c] for b in range(3))==0
        for i in range(2): assert sum(y[b][c]*u[b][i] for b in range(3))==0
    qf=[[F(x) for x in row] for row in q]
    vals=checks_q(qf)
    assert all(vals[:9]) and vals[9]==0 and vals[10]==F(1,198450)
    assert y[0][0]==1  # A2-based cycle maps to t^3, hence all its powers survive.
    return q,vals



def matrix_rank(rows):
    """Exact rank over QQ; used for the character-lattice weight matrices."""
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][j]
        a[r] = [x/d for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                d = a[i][j]
                a[i] = [x-d*y for x,y in zip(a[i],a[r])]
        r += 1
        if r == len(a):
            break
    return r


def coefficient_tori():
    triples = list(product(range(3), repeat=3))
    weights = []
    for a,b,c in triples:
        row = [0]*27
        for j in (3*a+b, 9+3*b+c, 18+3*c+a):
            row[j] += 1
        weights.append(row)
    remaining = [i for i,(a,b,c) in enumerate(triples) if a in (1,2)]
    assert matrix_rank(weights) == 19
    assert matrix_rank([weights[i] for i in remaining]) == 14
    index = {t:i for i,t in enumerate(triples)}
    invariants = []
    pairs = list(product((1,2),repeat=2))
    for i,j in pairs:
        e = [0]*27
        for a,b,c,sign in ((2,i,j,1),(1,i,j,-1),(2,0,0,1),(1,0,0,-1),
                           (2,i,0,-1),(1,i,0,1),(2,0,j,-1),(1,0,j,1)):
            e[index[(a,b,c)]] += sign
        assert all(sum(e[k]*weights[k][l] for k in range(27)) == 0 for l in range(27))
        invariants.append(e)
    # The section w0=w1=1, w2=normalized Q is integral, not just an isogeny.
    section_pairing = [[e[index[(2,i,j)]] for i,j in pairs] for e in invariants]
    assert section_pairing == [[int(i==j) for j in range(4)] for i in range(4)]
    return {'full_weight_rank':19, 'remaining_weight_rank':14,
            'full_quotient_dimension':8, 'remaining_quotient_dimension':4,
            'cross_ratio_characters_gauge_invariant':True,
            'integral_section_pairing':section_pairing,
            'split_kernel_dimension':4}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('build/four_hearts_corner_checks.json'))
    ap.add_argument('--mod-only',action='store_true',help='Skip independent QQ elimination; use full rank modulo the prime.')
    args=ap.parse_args()
    identities=universal_syzygies()
    tori=coefficient_tori()
    q=[[F(W[2][b][c],W[1][b][c]) for c in range(3)] for b in range(3)]
    vals=checks_q(q); assert all(vals)
    lam=[[q[i][j]*q[0][0]/(q[i][0]*q[0][j]) for j in (1,2)] for i in (1,2)]
    a,b=lam[0];c,d=lam[1]
    qnorm=[[F(1),F(1),F(1)],[F(1),a,b],[F(1),c,d]]
    factors=checks_q(qnorm)
    f10=(a-1)*(d-1)-(b-1)*(c-1)
    f11=b*c*(1-a)*(1-d)-a*d*(1-b)*(1-c)
    assert f10==factors[9] and f11==a*b*c*d*factors[10]
    assert all(factors)
    mod,blocks=quotient_dimensions(W,PRIME)
    qq=None
    if not args.mod_only:
        qq,qqblocks=quotient_dimensions(W,None)
        assert qq==mod and qqblocks==blocks
    qbad,badvals=rank_two_relations()
    qbad2=[[2520/F(x) for x in row] for row in qbad]
    bad2=checks_q(qbad2)
    assert all(bad2[:9]) and bad2[9]==80640 and bad2[10]==0
    result={'date':'2026-11-16','version':'hearts-v19','arithmetic':'Z and QQ; independent finite field',
      'coefficient_torus_checks':tori,
      'universal_six_point_syzygies_verified':identities,'universal_polynomial_variables':12,
      'potential_matrices':W,'witness_cross_ratios':[[str(x) for x in row] for row in lam],
      'normalized_nine_minors':[str(x) for x in factors[:9]],
      'last_two_polynomials':[str(f10),str(f11)],
      'prime':PRIME,'QQ_Hilbert_dimensions':qq,'mod_p_Hilbert_dimensions':mod,
      'degree_seven_blocks':blocks,'rank_two_example':qbad,
      'rank_two_reciprocal_determinant':str(badvals[10]),'reciprocal_example_determinant':str(bad2[9]),
      'rank_two_all_relations_verified':True,'nonzero_cycle_image':'t^3',
      'scope':'Finite arithmetic and universal syzygies only. The all-parameter finite-corner criterion is proved geometrically in the manuscript.',
      'AS_regularity_or_noetherianity_tested':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='degree_seven_blocks'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
