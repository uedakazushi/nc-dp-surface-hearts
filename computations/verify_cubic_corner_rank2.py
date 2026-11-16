#!/usr/bin/env python3
"""Exact cubic rank-2 corner obstructions; optional exhaustive F_7 test.

By default checks the explicit k[t]-representation of all 21 cyclic derivative
relations (27 scalar entries). --scan-f7 tests all 80 normalized F_7 points
satisfying the 11 necessary nonvanishing conditions; this is NOT a proof of
sufficiency over characteristic zero. Python standard library only.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path

r=(F(0),F(2),F(4)); s=(F(3),F(4),F(5))
h=(F(1),F(-2),F(1)); k=h
Q=[[r[b]+s[c] for c in range(3)] for b in range(3)]
Qi=[[1/Q[b][c] for c in range(3)] for b in range(3)]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def minors(A):
    return [A[i][c]*A[j][d]-A[i][d]*A[j][c]
            for i,j in combinations(range(3),2)
            for c,d in combinations(range(3),2)]

assert all(minors(Q)) and all(minors(Qi))
assert det3(Q)==0 and det3(Qi)==F(1,198450)
assert sum(h[b]*r[b] for b in range(3))==sum(h)==0
assert sum(k[c]*s[c] for c in range(3))==sum(k)==0

# A1=Q[t]^2, A2=B_b=C_c=Q[t].
# x1b=-t*[r_b,1], zc1=t*[1,s_c]^T, x2b=zc2=t, ybc=t*h_b*k_c.
relations=[]
for b,c in product(range(3),repeat=2):
    relations.append(-r[b]-s[c]+Q[b][c])  # d_y
for b in range(3):
    relations += [sum(h[b]*k[c] for c in range(3)),
                  sum(h[b]*k[c]*s[c] for c in range(3)),
                  sum(Q[b][c]*h[b]*k[c] for c in range(3))]
for c in range(3):
    relations += [sum(h[b]*k[c]*r[b] for b in range(3)),
                  sum(h[b]*k[c] for b in range(3)),
                  sum(Q[b][c]*h[b]*k[c] for b in range(3))]
assert len(relations)==27 and all(x==0 for x in relations)
assert h[0]*k[0]==1  # a 3-cycle maps to t^3; all powers survive

# Exchange A1 and A2, then normalize w'_1 to 1:
# the ratio matrix changes from Q to the entrywise reciprocal Qi.
Qrec=[[F(2520)*Qi[b][c] for c in range(3)] for b in range(3)]
assert all(minors(Qrec))
assert det3(Qrec)==80640
assert det3([[1/x for x in row] for row in Qrec])==0

result={'date':'2026-11-15','version':'corner-v3',
        'rank2_matrix':[[str(x) for x in row] for row in Q],
        'entrywise_reciprocal_scaled':[[str(x) for x in row] for row in Qrec],
        'rank2_reciprocal_determinant':str(det3(Qi)),
        'scaled_reciprocal_determinant':str(det3(Qrec)),
        'both_matrices_have_nine_nonzero_minors':True,
        'jacobian_scalar_entries_checked':len(relations),
        'surviving_cycle_coefficient':'1',
        'scope':'Both determinant-zero divisors imply infinite-dimensional C; 11 conditions not proved sufficient.'}

parser=argparse.ArgumentParser()
parser.add_argument('--scan-f7',action='store_true')
parser.add_argument('--output',type=Path,default=Path('build/cubic_corner_rank2_certificate.json'))
args=parser.parse_args()

if args.scan_f7:
    from verify_cubic_corner import corner_data
    p=7
    def allowed(a,b,c,d):
        if any(x==1 for x in (a,b,c,d)):return False
        if a==b or c==d or a==c or b==d:return False
        if (a*d-b*c)%p==0:return False
        if ((a-1)*(d-1)-(b-1)*(c-1))%p==0:return False
        ai,bi,ci,di=[pow(x,-1,p) for x in (a,b,c,d)]
        return ((ai-1)*(di-1)-(bi-1)*(ci-1))%p!=0

    def hilbert(Q):
        w=[[[1]*3 for _ in range(3)] for _ in range(3)]
        w[2]=Q
        arrows,outgoing,rels=corner_data(w)
        paths={0:{(v,v):[()] for v in range(1,9)}}
        dimensions=[8]
        for n in range(1,8):
            ps={}
            for (v,t),pr in paths[n-1].items():
                for path in pr:
                    for a in outgoing[t]:
                        ps.setdefault((v,arrows[a][1]),[]).append(path+(a,))
            paths[n]=ps
            if n==1:dimensions.append(21);continue
            bases={st:{} for st in ps}
            columns={st:{path:j for j,path in enumerate(pl)} for st,pl in ps.items()}
            for ell in range(n-1):
                for _,relation in rels:
                    sample=next(iter(relation))
                    rs,rt=arrows[sample[0]][0],arrows[sample[-1]][1]
                    for (v,t),prefixes in paths[ell].items():
                        if t!=rs:continue
                        for (u,z),suffixes in paths[n-2-ell].items():
                            if u!=rt:continue
                            st=(v,z);basis,idx=bases[st],columns[st]
                            for prefix in prefixes:
                                for suffix in suffixes:
                                    if len(basis)==len(idx):continue
                                    row={idx[prefix+path+suffix]:coef%p
                                         for path,coef in relation.items() if coef%p}
                                    while row:
                                        j=min(row);c=row[j]
                                        if j not in basis:
                                            inv=pow(c,-1,p)
                                            basis[j]={m:x*inv%p for m,x in row.items()}
                                            break
                                        for m,x in basis[j].items():
                                            val=(row.get(m,0)-c*x)%p
                                            if val:row[m]=val
                                            else:row.pop(m,None)
            dimensions.append(sum(len(columns[s])-len(bases[s]) for s in ps))
        return dimensions

    allowed_q=[(a,b,c,d) for a,b,c,d in product(range(1,p),repeat=4)
               if allowed(a,b,c,d)]
    assert len(allowed_q)==80
    for a,b,c,d in allowed_q:
        dimension=hilbert([[1,1,1],[1,a,b],[1,c,d]])
        assert dimension==[8,21,33,38,33,21,8,0],((a,b,c,d),dimension)
    result['F7_exhaustive']={'admissible_points':80,
       'hilbert_function':[8,21,33,38,33,21,8,0],
       'all_C7_zero':True,'scope':'F_7 only; NOT characteristic-zero sufficiency'}
    print('F7: checked all 80 normalized admissible points.')

args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 27 exact scalar Jacobian checks and two determinant obstructions.')
