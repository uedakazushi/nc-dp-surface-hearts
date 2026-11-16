#!/usr/bin/env python3
"""Exact single-root wall and explicit nodal anticanonical cubic.

Pure Python standard library: 9 cross-ratio minors, two determinants, six-point
incidence/conic condition, cubic polynomial identity and Hessian at node.
This does not prove categorical statements: see the corresponding TeX section.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from collections import defaultdict

Q=[[F(1),F(1),F(1)], [F(1),F(2),F(2)], [F(1),F(3),F(4)]]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

mins={f'{i}{j}|{k}{l}':Q[i][k]*Q[j][l]-Q[i][l]*Q[j][k]
      for i,j in combinations(range(3),2) for k,l in combinations(range(3),2)}
assert [k for k,v in mins.items() if not v]==['01|12']
assert det3(Q)==1 and det3([[1/x for x in row] for row in Q])==F(1,24)
P=[[1/Q[i][j] for i in range(3)] for j in range(3)]
pts=[tuple(P[j][i] for j in range(3)) for i in range(3)]
pts += [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
collinear=[]
for I in combinations(range(6),3):
    if not det3([list(pts[i]) for i in I]):collinear.append(tuple(i+1 for i in I))
assert collinear==[(1,2,4)]
mons2=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
E=[[x**a*y**b*z**c for a,b,c in mons2] for x,y,z in pts]
def rank(A):
    A=[[F(x) for x in row] for row in A];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        i=next((q for q in range(r,m) if A[q][j]),None)
        if i is None:continue
        A[r],A[i]=A[i],A[r]
        c=A[r][j];A[r]=[x/c for x in A[r]]
        for q in range(m):
            if q!=r and A[q][j]:
                c=A[q][j];A[q]=[a-c*b for a,b in zip(A[q],A[r])]
        r+=1
        if r==m:break
    return r
assert rank(E)==6

# Basis A,B,C,D of cubic sections of O(-K_S) through the six points.
polys=[
 {(2,1,0):F(1,3),(2,0,1):F(-1,3),(1,2,0):F(-1),(1,1,1):F(1)},
 {(2,1,0):F(7,12),(2,0,1):F(-7,12),(1,2,0):F(-1),(1,0,2):F(1)},
 {(2,1,0):F(1,6),(2,0,1):F(1,3),(1,2,0):F(-3,2),(0,2,1):F(1)},
 {(2,1,0):F(1,4),(2,0,1):F(1,4),(1,2,0):F(-3,2),(0,1,2):F(1)}
]
for v in polys:
    assert all(sum(coeff*(x**a*y**b*z**c) for (a,b,c),coeff in v.items())==0
               for x,y,z in pts)

def prod(a,b):
    out=defaultdict(F)
    for mon,x in a.items():
        for non,y in b.items():
            out[tuple(i+j for i,j in zip(mon,non))]+=x*y
    return {m:v for m,v in out.items() if v}

def multiply_powers(exp):
    out={(0,0,0):F(1)}
    for p,n in zip(polys,exp):
        for _ in range(n):out=prod(out,p)
    return out

# Integral projective cubic equation G(A,B,C,D).
terms={
 (3,0,0,0):23,(2,1,0,0):-22,(2,0,1,0):44,(2,0,0,1):-42,
 (1,2,0,0):8,(1,1,1,0):-16,(1,0,2,0):-24,(1,0,0,2):24,
 (0,2,1,0):8,(0,1,2,0):24,(0,1,1,1):-24
}
total=defaultdict(F)
for exp,c in terms.items():
    for mon,v in multiply_powers(exp).items():total[mon]+=c*v
assert not {mon:v for mon,v in total.items() if v}

# Image of line y=z is [A:B:C:D]=[0:0:1:1].
node=[F(0),F(0),F(1),F(1)]
def evaluate_derivatives(orders):
    out=F(0)
    for exp,c in terms.items():
        factor=c;e=list(exp)
        for i in orders:
            if not e[i]:factor=0;break
            factor*=e[i];e[i]-=1
        if factor:
            for j in range(4):factor*=node[j]**e[j]
            out+=factor
    return out

assert evaluate_derivatives([])==0
assert all(evaluate_derivatives([i])==0 for i in range(4))
H=[[evaluate_derivatives([i,j]) for j in (0,1,3)] for i in (0,1,3)]
assert det3(H)==-2304

out={
 'date':'2026-11-15','version':'classical-root-wall-v1',
 'Q':[[str(x) for x in row] for row in Q],
 'zero_minor_labels':[k for k,v in mins.items() if not v],
 'other_eight_minors_nonzero':True,
 'det_Q':str(det3(Q)),
 'det_componentwise_reciprocal_Q':str(det3([[1/x for x in row] for row in Q])),
 'six_points':[[str(x) for x in p] for p in pts],
 'only_collinear_triple':collinear[0],
 'conic_evaluation_rank':rank(E),
 'cubic_identity_verified_exactly':True,
 'node_projective_coordinates':[str(x) for x in node],
 'node_hessian_affine_A_B_D':[[str(x) for x in row] for row in H],
 'node_hessian_determinant':str(det3(H)),
 'scope':'Exact explicit algebra; categorical arguments are in cubic_corner_root_walls.tex.'
}
path=Path('build/cubic_corner_root_wall_certificate.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS: unique root wall',collinear,'only zero minor',out['zero_minor_labels'])
print('PASS: cubic equation identity and nodal Hessian determinant',det3(H))
