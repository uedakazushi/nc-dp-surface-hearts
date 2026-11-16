#!/usr/bin/env python3
"""Exact Dynkin root and zigzag Ext/Kuranishi arithmetic for del Pezzo d=1..6.

Checks E_(9-d) roots, simple-root Dynkin pairings, negative intersections
for all nonsimple positive roots, tree/forest leaf elimination and the
primary quadratic Maurer--Cartan branch count. Rains sheaf existence,
Yoneda nondegeneracy and intrinsic formality are THEOREMS imported from
primary literature, not verified by this code.
"""
from itertools import combinations
from pathlib import Path
import json

def dot(u,v):
    return u[0]*v[0]-sum(x*y for x,y in zip(u[1:],v[1:]))

def positive_roots(r):
    roots=[]
    for i,j in combinations(range(r),2):
        m=[0]*r;m[i]=-1;m[j]=1
        roots.append((0,)+tuple(m))
    for inds in combinations(range(r),3):
        roots.append((1,)+tuple(int(i in inds) for i in range(r)))
    for inds in combinations(range(r),6):
        roots.append((2,)+tuple(int(i in inds) for i in range(r)))
    if r==8:
        for i in range(r):
            roots.append((3,)+tuple(2 if j==i else 1 for j in range(r)))
    return roots

def simples(r):
    ans=[(1,)+(1,1,1)+(0,)*(r-3)]
    for i in range(r-1):
        m=[0]*r;m[i]=-1;m[i+1]=1
        ans.append((0,)+tuple(m))
    return ans

def root_coefficients(root):
    r=len(root)-1
    a=root[0]; b=root[1:]
    c=[0]*r;c[0]=a
    for i in range(1,r):
        if i==1:c[i]=c[0]-b[0]
        elif i<=3:c[i]=c[0]+c[i-1]-b[i-1]
        else:c[i]=c[i-1]-b[i-1]
    s=simples(r)
    assert root==tuple(sum(c[i]*s[i][j] for i in range(r))
                       for j in range(r+1))
    return c

expected={
 3:('A2+A1',8,1,8),4:('A4',20,3,14),
 5:('D5',40,4,18),6:('E6',72,5,22),
 7:('E7',126,6,26),8:('E8',240,7,30)
}
out={}
for r in range(3,9):
    simple=simples(r);roots=positive_roots(r)
    name,number,edge_count,extdim=expected[r]
    assert len(roots)*2==number
    assert all(dot(z,z)==-2 for z in roots)
    edges=[(i,j) for i,j in combinations(range(r),2)
           if dot(simple[i],simple[j])==1]
    assert len(edges)==edge_count
    assert all(dot(simple[i],simple[j]) in (0,1)
               for i,j in combinations(range(r),2))
    adj={i:set() for i in range(r)}
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    negative_witnesses=0
    for root in roots:
        cc=root_coefficients(root)
        assert all(x>=0 for x in cc)
        if root in simple:continue
        assert any(cc[i]>0 and dot(root,simple[i])<0 for i in range(r))
        negative_witnesses+=1
    assert negative_witnesses==(number//2-r)
    assert 2*r+2*len(edges)==extdim
    rest={i:set(links) for i,links in adj.items()}
    leaf_order=[]
    while any(rest[i] for i in rest):
        leaf=next(i for i in rest if len(rest[i])==1)
        dest=next(iter(rest[leaf]))
        leaf_order.append((leaf,dest))
        rest[dest].remove(leaf);rest[leaf].remove(dest)
    assert len(leaf_order)==len(edges)
    out[str(9-r)]={
       'root_system':name,'root_rank':r,'root_count':number,
       'simple_irreducible_root_classes':r,
       'non_simple_positive_roots_with_negative_pairing':negative_witnesses,
       'zigzag_edges':edges,'Ext0_dim':r,'Ext1_dim':2*len(edges),
       'Ext2_dim':r,'total_Ext_dimension':extdim,
       'primary_quadratic_Kuranishi_components':2**len(edges),
       'framed_formal_component_dimension':len(edges),
       'forest_leaf_elimination_order':leaf_order}
certificate={
 'date':'2026-11-15','version':'resonance-zigzag-v2',
 'all_degrees':out,
 'proved_import':'Liu--Wang, Journal of Algebra 677 (2025), Theorem 1.1: path-graded zigzag intrinsically formal for finite ADE trees over characteristic zero. Isolated A1 degree 0/2 component formal by degree.',
 'scope':'Exact root arithmetic and leaf-elimination check only. Sheaf existence, Yoneda products and intrinsic formality are from separately cited mathematical theorems, not this Python computation.',
 'not_calculated':'Explicit finite A=R/(g-1) module matrices, mixed connecting delta rank, all-q derived equivalence.'
}
path=Path('build/resonance_zigzag_certificate.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS:',[(k,v['root_count'],v['total_Ext_dimension'],
 v['primary_quadratic_Kuranishi_components']) for k,v in out.items()])
