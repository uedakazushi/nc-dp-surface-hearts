#!/usr/bin/env python3
"""Exact Picard lattice verification for the cubic corner's uniform C_7 cutoff.

Coordinates (d,m_1,...,m_6) represent d*h - sum(m_i*e_i).
Checks all 27 (-1)-curves, four blowdown line classes, and 13
nef-and-big/Kawamata-Viehweg divisor inputs. This verifies numerical
hypotheses, not the geometric sheaf multiplication surjectivity by itself.
Standard Python library only. Output goes to build/, never tracked.
"""
from itertools import combinations
import json
from pathlib import Path

def plus(A,B):return tuple(x+y for x,y in zip(A,B))
def minus(A,B):return tuple(x-y for x,y in zip(A,B))
def mult(n,A):return tuple(n*x for x in A)
def intersect(A,B):return A[0]*B[0]-sum(x*y for x,y in zip(A[1:],B[1:]))
H=(3,1,1,1,1,1,1); h=(1,0,0,0,0,0,0)
def e(i):return tuple(0 if j==0 else -int(j==i) for j in range(7))

curves={f'e{i}':e(i) for i in range(1,7)}
for i,j in combinations(range(1,7),2):
    curves[f'l{i}{j}']=minus(minus(h,e(i)),e(j))
for i in range(1,7):
    q=mult(2,h)
    for j in range(1,7):
        if j!=i:q=minus(q,e(j))
    curves[f'q{i}']=q
assert len(curves)==27
assert all(intersect(C,C)==-1 and intersect(H,C)==1 for C in curves.values())
D={1:(-2,-1,-1,-1,-1,-1,-1),2:(-1,-1,-1,-1,0,0,0)}
Lm={a:minus(H,D[a]) for a in D}
Lp={a:plus(H,D[a]) for a in D}
for kind,cs in [('H_minus_D',Lm),('H_plus_D',Lp)]:
    for a,L in cs.items():
        contracted=[name for name,C in curves.items() if intersect(L,C)==0]
        assert len(contracted)==6
        assert all(intersect(curves[x],curves[y])==0 for x,y in combinations(contracted,2))
        assert intersect(L,L)==1 and intersect(L,H)==3
        assert all(intersect(L,C)>=0 for C in curves.values())
for a,L in Lm.items():
    assert all(intersect(L,e(i))==2 for i in range(1,4))
for a,L in Lp.items():
    assert all(intersect(L,curves[f'q{j}'])==2 for j in range(4,7))

kv={}
for a in (1,2):
    kv[f'3H-D{a}']=minus(mult(3,H),D[a])
    kv[f'3H+D{a}']=plus(mult(3,H),D[a])
for i in (1,2,3):
    for j in (4,5,6):
        kv[f'3H-e{i}-h+e{j}']=plus(minus(minus(mult(3,H),e(i)),h),e(j))
for name,A in kv.items():
    vals=[intersect(A,C) for C in curves.values()]
    assert intersect(A,A)>0 and min(vals)>=0,(name,intersect(A,A),min(vals))
for i in (1,2,3):
    A=minus(mult(3,H),e(i))
    assert all(intersect(A,C)>0 for C in curves.values())
for j in (4,5,6):
    pencil=minus(h,e(j))
    assert intersect(pencil,pencil)==0
    assert all(intersect(pencil,C)>=0 for C in curves.values())
    q=curves[f'q{j}']
    assert intersect(q,q)==-1 and intersect(H,q)==1
    assert intersect(pencil,q)==2
    A=plus(mult(2,H),pencil)
    assert all(intersect(A,C)>0 for C in curves.values())
assert intersect(H,H)==3
assert all(intersect(H,D[a])==0 and intersect(D[a],D[a])==-2 for a in D)

certificate={
    'date':'2026-11-15','version':'corner-c7-v1','characteristic':0,
    'K2':intersect(H,H),
    'contracted_curves_minus':{
       str(a):[n for n,C in curves.items() if intersect(L,C)==0] for a,L in Lm.items()},
    'contracted_curves_plus':{
       str(a):[n for n,C in curves.items() if intersect(L,C)==0] for a,L in Lp.items()},
    'nef_big_KV_inputs':{
      name:{'square':intersect(A,A),
            'min_27_curve_intersection':min(intersect(A,C) for C in curves.values())}
      for name,A in kv.items()},
    'scope':'Numerical geometry, not a stand-alone proof of path factorization; see cubic_corner_uniform_cutoff.tex.'
}
out=Path('build/cubic_corner_c7_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 27 (-1)-curves, four blowdown line classes, 13 nef-big vanishing inputs.')
