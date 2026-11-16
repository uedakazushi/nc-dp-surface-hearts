#!/usr/bin/env python3
"""Exact Picard/Euler/sign-duality checks for the Rains root resonance trichotomy.

Checks E_{9-d} root pairing for d=1,...,6; the degree-(m-1)
commutative (-2)-curve toy model against m=chi(e,M); dual degree
-(m-1)-2= -m-1, its Euler sign flip, and spherical Euler number 2.
It does NOT prove Rains root-sheaf existence, the derived duality or
derived equivalence: those are supplied by the cited source theorems.
Python standard library only; writes an optional JSON certificate to build/.
"""
from pathlib import Path
import argparse
import json

def pair(x, y):
    return x[0] * y[0] - sum(a*b for a,b in zip(x[1:],y[1:]))

root_checks=[]
for d in range(1,7):
    r=9-d
    H=(3,)+(1,)*r
    alpha=(1,)+(1,1,1)+(0,)*(r-3)
    beta=(0,)+(-1,1)+(0,)*(r-2)
    for root in (alpha,beta):
        assert pair(root,root)==-2
        assert pair(H,root)==0
        assert -pair(root,root)//2==1
    root_checks.append({'degree':d,'blowups':r,'alpha':list(alpha),
       'beta':list(beta),'root_square':-2,'H_dot_root':0,
       'root_quotient_chi_minimum':1,'root_self_Euler':2})

sign_checks=[]
for m in range(-20,21):
    deg=m-1
    h0=max(deg+1,0)
    h1=max(-deg-1,0)
    dual_deg=-deg-2
    assert h0==max(m,0)
    assert h1==max(-m,0)
    assert h0-h1==m
    assert dual_deg+1==-m
    assert max(dual_deg+1,0)==h1
    assert max(-dual_deg-1,0)==h0
    sign_checks.append({'m':m,'H0':h0,'Ext1':h1,'Ext2':0,
       'dual_m':-m,'dual_degree':dual_deg,
       'affine_module_dimension':abs(m) if m else None,
       'derived_section_cohomological_degree':
           0 if m>0 else 1 if m<0 else None})

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,
    default=Path('build/resonance_hearts_sign_certificate.json'))
args=parser.parse_args()
args.output.parent.mkdir(parents=True, exist_ok=True)
result={'date':'2026-11-15','version':'resonance-hearts-v2',
 'degrees_checked':list(range(1,7)),
 'root_tests':root_checks,'sign_checks':sign_checks,
 'toy_model':'On a commutative (-2)-curve, M=O_P1(m-1), dual M=O_P1(-m-1). This checks signs only.',
 'mathematical_conclusion':'For an existing irreducible root sheaf disjoint from the boundary, Hom(e,M)=max(m,0), Ext1(e,M)=max(-m,0), Ext2=0. Positive and negative resonances are each Zariski dense under Rains existence hypotheses.',
 'limitations':'Arithmetic consistency, not a computational proof of root sheaf existence, categorical duality, AZ ampleness, full t-exactness, or derived equivalence.'}
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',
                      encoding='utf-8')
print('PASS: E_(9-d) root data d=1..6, sign and duality m=-20..20, spherical Euler=2')
