#!/usr/bin/env python3
"""Exact rational test of cubic corner cross ratios and a bad 2x2 minor."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json

W1=[[2,1,1],[-1,2,-4],[-1,-3,1]]
W2=[[1,1,2],[-1,-1,-1],[1,1,1]]
def cross(A,B):
    q=[[F(B[i][j],A[i][j]) for j in range(3)] for i in range(3)]
    return [[q[i][j]*q[0][0]/(q[i][0]*q[0][j]) for j in (1,2)] for i in (1,2)]
good=cross(W1,W2)
assert good==[[F(-1,4),F(1,16)],[F(1,6),F(-1,4)]]
Q=[[F(1)]*3,[F(1),*good[0]],[F(1),*good[1]]]
minors=[Q[i][k]*Q[j][l]-Q[i][l]*Q[j][k]
        for (i,j) in combinations(range(3),2)
        for (k,l) in combinations(range(3),2)]
assert len(minors)==9 and all(minors)
# All entries nonzero; the indicated 2x2 submatrix alone is rank one.
qbad=[[F(x) for x in row] for row in [[1,2,3],[4,8,5],[6,7,11]]]
assert qbad[0][0]*qbad[1][1]==qbad[0][1]*qbad[1][0]
assert qbad[0][0]*qbad[1][2]!=qbad[0][2]*qbad[1][0]
A=[[F(2+b+3*c) for c in range(3)] for b in range(3)]
B=[[A[b][c]*qbad[b][c] for c in range(3)] for b in range(3)]
T=[[F(1),F(-1)],[F(-1),F(1)]]
r=[F(1),F(4)]
s=[F(1),F(2)]
X=[[F(1) if b<2 else F(0) for b in range(3)],
   [-F(1)/r[b] if b<2 else F(0) for b in range(3)]]
Z=[[F(1),F(1)/s[c]] if c<2 else [F(0),F(0)] for c in range(3)]
Y=[[T[b][c]/A[b][c] if b<2 and c<2 else F(0) for c in range(3)] for b in range(3)]
W=[A,B]
assert all(sum(W[a][b][c]*Y[b][c]*Z[c][a] for c in range(3))==0
           for a,b in product(range(2),range(3)))
assert all(sum(W[a][b][c]*X[a][b]*Y[b][c] for b in range(3))==0
           for a,c in product(range(2),range(3)))
assert all(sum(W[a][b][c]*Z[c][a]*X[a][b] for a in range(2))==0
           for b,c in product(range(3),range(3)))
assert X[0][0]*Y[0][0]*Z[0][0]!=0
rr=[F(2),F(3),F(5)]; ss=[F(7),F(11),F(13)]
A2=[[A[b][c]*F(2+b+3*c) for c in range(3)] for b in range(3)]
B2=[[B[b][c]*F(2+b+3*c)*rr[b]*ss[c] for c in range(3)] for b in range(3)]
assert cross(A2,B2)==cross(A,B)
result={
 'version':'hearts-v3/torus-v1',
 'good_cross_ratios':[[str(x) for x in row] for row in good],
 'nine_good_minors':[str(x) for x in minors],
 'bad_ratio_matrix':[[str(x) for x in row] for row in qbad],
 'bad_minor_zero':True,
 'nonzero_cycle':True,
 'jacobian_relations_checked':21,
 'gauge_invariance':True,
 'scope':'Exact rational examples only; universal proof in cubic_heart_corner.tex'
}
out=Path('build/cubic_corner_torus_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: four cross-ratios, nine good minors, 21 Jacobian relations, nonzero cycle')
