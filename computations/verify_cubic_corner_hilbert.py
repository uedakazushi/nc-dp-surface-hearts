#!/usr/bin/env python3
"""Exact Picard-lattice audit for the uniform Hilbert series of cubic corners.

Computes RR Hom dimensions, 27 (-1)-curve intersections, all four pairs
of blowdown line systems, pencil-trick kernel Euler data, and graded
dimension bookkeeping. The geometric multiplication map arguments
remain in papers/sections/cubic_corner_hilbert_series.tex.
No third-party dependencies; cache/output written under build/.
"""
from itertools import combinations, product
from pathlib import Path
import json

h=(1,0,0,0,0,0,0)
H=(3,1,1,1,1,1,1)
zero=(0,0,0,0,0,0,0)
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def neg(u):return tuple(-a for a in u)
def sub(u,v):return add(u,neg(v))
def mul(n,u):return tuple(n*x for x in u)
def pair(u,v):return u[0]*v[0]-sum(x*y for x,y in zip(u[1:],v[1:]))
def e(i):return (0,)+tuple(-int(j==i) for j in range(1,7))
def chi(d):
    numerator=pair(d,add(d,H))
    assert numerator%2==0
    return 1+numerator//2

D={1:(-2,-1,-1,-1,-1,-1,-1),2:(-1,-1,-1,-1,0,0,0)}
Bi={i:e(i) for i in range(1,4)}
Gj={j:sub(h,e(j)) for j in range(4,7)}
qj={j:sub(H,Gj[j]) for j in Gj}
minus={a:sub(H,D[a]) for a in D}
plus={a:add(H,D[a]) for a in D}

curves={f'e{i}':e(i) for i in range(1,7)}
for i,j in combinations(range(1,7),2):curves[f'l{i}{j}']=sub(sub(h,e(i)),e(j))
for j in range(1,7):
    q=mul(2,h)
    for i in range(1,7):
        if i!=j:q=sub(q,e(i))
    curves[f'q{j}']=q
assert len(curves)==27
assert all(pair(c,c)==-1 and pair(H,c)==1 for c in curves.values())

classes={**{f'A{a}':d for a,d in D.items()},
         **{f'B{i}':d for i,d in Bi.items()},
         **{f'C{j}':d for j,d in Gj.items()}}
level={'A':0,'B':1,'C':2}
totalHom=[]
for n in range(8):
    dimensions=[]
    for s,t in product(classes,repeat=2):
        source,end=level[s[0]],level[t[0]]
        if (source+n)%3!=end:continue
        cut=(source+n)//3
        dimensions.append(chi(add(mul(cut,H),sub(classes[t],classes[s]))))
    totalHom.append(sum(dimensions))
assert totalHom==[8,21,42,74,105,147,206,252]
# BeB ranks come from independent geometric multiplication lemmas in the paper.
through_e=[0,0,9,36,72,126,198,252]
hilbert=[a-b for a,b in zip(totalHom,through_e)]
assert hilbert==[8,21,33,38,33,21,8,0] and sum(hilbert)==162

assert chi(H)==4 and chi(mul(2,H))==10
for a in D:assert chi(minus[a])==chi(plus[a])==3
for i in Bi:
    assert chi(sub(H,Bi[i]))==2
    assert chi(add(H,Bi[i]))==5
    assert chi(sub(mul(2,H),Bi[i]))==7
for j in Gj:
    assert chi(Gj[j])==2 and chi(qj[j])==1
    assert chi(add(H,Gj[j]))==7 and chi(add(H,qj[j]))==5
for i in Bi:
    for j in Gj:
        qminus=sub(qj[j],Bi[i])
        assert pair(qminus,qj[j])==-2
        assert sub(qminus,qj[j])==neg(Bi[i])

# The kernel H^0(2E) has dimension one, but chi(2E)=0:
# do not silently substitute Euler characteristic for h^0 of fixed curves.
for i,k in product(Bi,repeat=2):
    assert chi(add(Bi[i],Bi[k]))==(0 if i==k else 1)
for j,k in product(Gj,repeat=2):
    assert chi(add(qj[j],qj[k]))==(0 if j==k else 1)

net=[]
for a,b in product((1,2),repeat=2):
    L,M=minus[a],plus[b]
    exceptional=[name for name,E in curves.items() if pair(L,E)==0]
    conics=[name for name in exceptional if pair(M,curves[name])==2]
    assert len(exceptional)==6 and len(conics)>=3
    assert all(pair(curves[x],curves[y])==0 for x,y in combinations(exceptional,2))
    assert pair(L,L)==pair(M,M)==1 and pair(L,H)==pair(M,H)==3
    net.append({'pair':[a,b],'intersection_LM':pair(L,M),
                'L_contracts':exceptional,
                'M_conic_images':conics})

# Kernels for the two A->C pencil multiplications.
for j in Gj:
    assert sub(minus[1],Gj[j])==sub(mul(2,qj[j]),e(j))
    three=sum((0,),()) if False else zero
    for i,k in ((1,2),(1,3),(2,3)):
        ell=sub(sub(h,e(i)),e(k))
        assert pair(sub(minus[2],Gj[j]),ell)==-1
        three=add(three,ell)
    remaining=sub(sub(minus[2],Gj[j]),three)
    other=[i for i in (4,5,6) if i!=j]
    assert remaining==neg(add(e(other[0]),e(other[1])))

result={
 'date':'2026-11-15','version':'corner-hilbert-v1',
 'geometric_hypothesis':'six ordered points in general position over char 0',
 'full_Hom_dimensions':totalHom,
 'through_structure_vertex_dimensions':through_e,
 'corner_hilbert_dimensions':hilbert,'total_dimension':162,
 'exceptional_curves_checked':27,
 'four_blowdown_pairs':net,
 'proof_scope':'Exact integer Picard/RR and bookkeeping checks only. Sheaf multiplication surjectivity/injectivity is proved in the TeX paper, not by this code.'
}
out=Path('build/cubic_corner_hilbert_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: Hilbert',hilbert,'total',sum(hilbert))
print('PASS: 27 curves and all four net injectivity numerical hypotheses')
