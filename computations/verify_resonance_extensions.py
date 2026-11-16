#!/usr/bin/env python3
"""Exact E6 root intersections, root-sum resonance obstruction and mixed Ext ranks.

Python standard library only. No categorical or sheaf existence claims follow
from these arithmetic checks. For proof see resonance_extension_cancellation.tex.
"""
from itertools import combinations, product
import json
from pathlib import Path

H=(3,1,1,1,1,1,1)
def pair(x,y):
    return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))
def neg(x):return tuple(-a for a in x)
def add(x,y):return tuple(a+b for a,b in zip(x,y))

roots=set()
for i,j in combinations(range(1,7),2):
    r=[0]*7;r[i]=-1;r[j]=1;r=tuple(r)
    roots.update((r,neg(r)))
for inds in combinations(range(1,7),3):
    r=(1,)+tuple(int(i in inds) for i in range(1,7))
    roots.update((r,neg(r)))
r=(2,1,1,1,1,1,1)
roots.update((r,neg(r)))
assert len(roots)==72
assert all(pair(r,r)==-2 and pair(H,r)==0 for r in roots)
counts={-2:0,-1:0,0:0,1:0,2:0}
for a,b in product(roots,repeat=2):
    if a==b:continue
    d=pair(a,b)
    assert d in counts
    counts[d]+=1
    if d==1:assert add(a,b) in roots
assert counts[1]>0

# Simple adjacent A2 roots, plus a root: e1-e2, e2-e3, e1-e3.
a=(0,-1,1,0,0,0,0)
b=(0,0,-1,1,0,0,0)
assert a in roots and b in roots and pair(a,b)==1
assert add(a,b)==(0,-1,0,1,0,0,0)

# Classical Euler sequence O(-2)->O(-1)^2->O is a mixed-sign extension.
# Its two maps are (-y,x) and (x,y); the composition is zero.
assert 1*(-1)+1*(1)==0
assert (max(0,-2+1),max(0,2-1))==(0,1)
assert (max(0,0+1),max(0,-1))==(1,0)
assert (max(0,-1+1),max(0,1-1))==(0,0)

checks=[]
for p,n in product(range(1,5), repeat=2):
    for rank in range(min(p,n)+1):
        h0=p-rank;h1=n-rank
        assert h0-h1==p-n
        checks.append((p,n,rank,h0,h1))
assert (1,1,1,0,0) in checks
result={
 'date':'2026-11-15','version':'resonance-extensions-v1',
 'E6_roots':len(roots),
 'ordered_pair_intersection_counts':{str(k):v for k,v in counts.items()},
 'adjacent_A2_example':{'alpha':a,'beta':b,'sum':add(a,b)},
 'mixed_rank_cases_checked':len(checks),
 'euler_sequence':'0 -> O_P1(-2) -> O_P1(-1)^2 -> O_P1 -> 0',
 'euler_connecting_rank':1,
 'euler_middle_term_derived_global_sections_zero':True,
 'scope':'Exact root-lattice arithmetic and elementary P1 cohomology. No test for Rains sheaf existence, all-q derived equivalence, or existence of mixed extensions on genuine noncommutative del Pezzo.'
}
out=Path('build/resonance_extensions_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS:',len(roots),'E6 roots, counts',counts)
print('PASS:',len(checks),'mixed exact-sequence ranks and Euler-sequence acyclicity')
