#!/usr/bin/env python3
"""Exact E6 maximal-resonance arithmetic and a mixed A2 root witness.

Standard library only. The script checks rational elliptic multiples, 20
triple collinearity determinants, the conic determinant, all E6 roots
and the Kronecker-rank bookkeeping for mixed extensions.
Rains root-sheaf existence and full derived faithfulness are NOT computed.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

a,b=-1,1
q=(F(0),F(1))
exponents=(1,3,2,5,7,11)

def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and y==-v: return None
    slope=(3*x*x+a)/(2*y) if P==Q else (v-y)/(u-x)
    xx=slope*slope-x-u
    return xx,slope*(x-xx)-y

multiples={0:None}
P=None
for n in range(1,max(exponents)+1):
    P=add(P,q)
    assert P is not None and P[1]**2==P[0]**3+a*P[0]+b
    multiples[n]=P
assert multiples[2]==(F(1,4),F(-7,8))
# By Nagell--Lutz, nonintegral x(2q) proves q is non-torsion.

points=[(multiples[n][0],multiples[n][1],F(1)) for n in exponents]
def det(A):
    mat=[[F(v) for v in row] for row in A]
    n=len(mat); d=F(1)
    assert all(len(row)==n for row in mat)
    for k in range(n):
        z=next((i for i in range(k,n) if mat[i][k]),None)
        if z is None:return F(0)
        if z!=k: mat[k],mat[z]=mat[z],mat[k];d=-d
        pivot=mat[k][k];d*=pivot
        for i in range(k+1,n):
            c=mat[i][k]/pivot
            for j in range(k+1,n):mat[i][j]-=c*mat[k][j]
            mat[i][k]=0
    return d

triples=[det([points[i] for i in ids]) for ids in combinations(range(6),3)]
assert len(triples)==20 and all(triples)
conic=det([[x*x,x*y,y*y,x,y,F(1)] for x,y,_ in points])
assert conic

# Roots are represented by a*h - sum b_i*e_i.
roots=[]
for i,j in combinations(range(6),2):
    v=[0]*6;v[i]=-1;v[j]=1
    roots.extend([(0,tuple(v)),(0,tuple(-u for u in v))])
for ids in combinations(range(6),3):
    v=tuple(int(i in ids) for i in range(6))
    roots.extend([(1,v),(-1,tuple(-u for u in v))])
roots.extend([(2,(1,)*6),(-2,(-1,)*6)])
assert len(roots)==72

def dot(r,s):return r[0]*s[0]-sum(u*v for u,v in zip(r[1],s[1]))
def index(r):return sum(u*n for u,n in zip(r[1],exponents))
assert all(dot(r,r)==-2 and 3*r[0]==sum(r[1]) for r in roots)
assert all(index(r)!=0 for r in roots)
simples=[(1,(1,1,1,0,0,0))]
for i in range(5):
    v=[0]*6;v[i]=-1;v[i+1]=1
    simples.append((0,tuple(v)))
ms=[index(r) for r in simples]
assert ms==[6,2,-1,3,2,4]
for (h,v) in roots:
    c0=h;c1=c0-v[0];c2=c0+c1-v[1]
    c3=c0+c2-v[2];c4=c3-v[3];c5=c4-v[4]
    assert c5==v[5]
    assert sum(c*m for c,m in zip((c0,c1,c2,c3,c4,c5),ms))==index((h,v))
alpha,beta=simples[1],simples[2]
assert dot(alpha,beta)==1 and (index(alpha),index(beta))==(2,-1)
assert index((0,(-1,0,1,0,0,0)))==1
# For a copies of M_alpha and b copies of M_beta:
# delta=d tensor T, rank(delta)<=min(a,b).  Thus H0>=a.
rank_checks=0
for copies_a in range(1,6):
    for copies_b in range(8):
        for rank in range(min(copies_a,copies_b)+1):
            H0=2*copies_a-rank
            H1=copies_b-rank
            assert H0>=copies_a>0 and H0-H1==2*copies_a-copies_b
            rank_checks+=1

# Uniform classification of roots of E_(9-r), r=3,...,8.
# All positive h-coefficient roots have nonnegative exceptional multiplicities.
root_counts={3:8,4:20,5:40,6:72,7:126,8:240}
uniform_sample=(1,3,2,5,7,11,13,17)
degree_data={}
for r in range(3,9):
    nr=uniform_sample[:r]
    root_list=[]
    for i,j in combinations(range(r),2):
        v=[0]*r;v[i]=-1;v[j]=1
        root_list += [(0,tuple(v)),(0,tuple(-x for x in v))]
    for ids in combinations(range(r),3):
        v=tuple(int(i in ids) for i in range(r))
        root_list += [(1,v),(-1,tuple(-x for x in v))]
    for ids in combinations(range(r),6):
        v=tuple(int(i in ids) for i in range(r))
        root_list += [(2,v),(-2,tuple(-x for x in v))]
    if r==8:
        for i in range(r):
            v=tuple(2 if j==i else 1 for j in range(r))
            root_list += [(3,v),(-3,tuple(-x for x in v))]
    assert len(root_list)==root_counts[r]
    for aa,bb in root_list:
        assert 3*aa==sum(bb) and aa*aa-sum(x*x for x in bb)==-2
        assert sum(x*n for x,n in zip(bb,nr))!=0
    root_simples=[(1,(1,1,1)+(0,)*(r-3))]
    for i in range(r-1):
        bb=[0]*r;bb[i]=-1;bb[i+1]=1
        root_simples.append((0,tuple(bb)))
    mm=[sum(x*n for x,n in zip(bb,nr)) for aa,bb in root_simples]
    assert mm[:3]==[6,2,-1]
    degree_data[str(9-r)]={'blowups':r,'root_count':len(root_list),
                           'all_root_indices_nonzero':True,
                           'simple_indices':mm}

result={
  'date':'2026-11-15','version':'resonance-maximal-roots-v2',
  'elliptic_curve':'y^2=x^3-x+1','q':['0','1'],
  'two_q':['1/4','-7/8'],
  'non_torsion_reason':'Nagell--Lutz; 2q has nonintegral x coordinate',
  'six_multipliers':list(exponents),
  'six_rational_points':[[str(c) for c in p] for p in points],
  'nonzero_triple_determinants':20,'nonzero_conic_determinant':True,
  'root_count':72,'all_root_indices_nonzero':True,
  'simple_root_indices':ms,
  'actual_A2_pair':{'alpha':'e1-e2','beta':'e2-e3',
                    'Euler_alpha':2,'Euler_beta':-1,'intersection':1,
                    'Ext1_dimension_from_Rains':1},
  'two_step_extension_rank_cases_checked':rank_checks,
  'all_degrees_1_through_6':degree_data,
  'scope':'Exact arithmetic only (E6 rational witness and integer root systems in degrees 1..6). Rains effectiveness for simple roots is primary-source input. No affine-module matrices or delta rank were computed.'
}
out=Path('build/resonance_maximal_a2_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 20 triples, conic, 72 roots, simple indices',ms,'rank checks',rank_checks)
