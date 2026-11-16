#!/usr/bin/env python3
"""Exact K0/Picard and right-normalized boundary checks (hearts-v23).

Checks the two distinct shift conventions, actual-tuple recovery, all nine
boundary-first candidates, and signed K0 mutation including the explicit
cohomological re-shift of the last three objects. The geometric identification
uses the primary-source functor arguments in the manuscript, not these finite
checks. This code does not establish author-endorsed corrections to AOU.
Python standard library only. Run from the repository/bundle root.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product, permutations
import json
from pathlib import Path
from random import Random


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def inverse(a):
    n=len(a)
    m=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next((i for i in range(j,n) if m[i][j]),None)
        if p is None: raise ValueError('Singular matrix')
        m[p],m[j]=m[j],m[p]
        c=m[j][j];m[j]=[x/c for x in m[j]]
        for i in range(n):
            if i!=j:
                c=m[i][j];m[i]=[x-c*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]


def numeric_from_basis(v, r):
    """Return (rank, h coefficient, exceptional coefficients..., Euler)."""
    return (sum(v[r:]),-2*v[r]-v[r+1],*v[:r],v[r+2])


def tensor_H(x, r):
    u,a,*rest=x; ci=rest[:-1];c=rest[-1]
    delta=3*a+sum(ci);d=9-r
    return (u,a+3*u,*(b-u for b in ci),c+delta+u*d)


def determinant(x):
    """Exponents of L, O(p_i), q in det F(x)."""
    u,a,*rest=x;ci=rest[:-1];c=rest[-1]
    return (a,*ci,c-u)


def boundary_on_determinant(x, r):
    u,a,*rest=x;ci=rest[:-1];c=rest[-1]
    delta=3*a+sum(ci);d=9-r
    z=list(determinant(x));z[0]+=3*u
    for i in range(r):z[i+1]-=u
    z[-1]+=delta+u*d
    return tuple(z)


# A line class: degree; coefficients of AJ(L0), b (sigma=t_b), D=sum p_i;
# two independent E[3] coordinates. The AJ part is a formal abelian group.
def line(degree,l=0,b=0,D=0,e1=0,e2=0):
    return (degree,l,b,D,e1%3,e2%3)


def add(*classes):
    return line(*(sum(t) for t in zip(*classes)))


def scale(k,x):
    return line(*(k*a for a in x))


def push(k,x):
    """t_{k b,*} on line bundles."""
    d,l,b,D,e1,e2=x
    return line(d,l,b+k*d,D,e1,e2)



def right_normalized_shift_checks():
    """Invert both actual endofunctors, not just their determinant degrees."""
    L0=line(3,1)
    positive=lambda m: push(1,add(m,L0))
    negative=lambda m: add(push(-1,m),scale(-1,L0))
    alternate=lambda m: add(L0,push(-1,m))
    alternate_inverse=lambda m: push(1,add(m,scale(-1,L0)))
    count=0
    for degree,l,coefficient in product(range(-6,7),range(-2,3),range(-2,3)):
        m=line(degree,l,coefficient,D=1,e1=1,e2=2)
        assert negative(positive(m))==positive(negative(m))==m
        assert alternate_inverse(alternate(m))==alternate(alternate_inverse(m))==m
        count+=1
    one=line(0);L1=push(-1,L0)
    v1=negative(one);v2=negative(v1)
    assert v1==scale(-1,L0)
    assert v2==scale(-1,add(L0,L1))
    assert alternate_inverse(one)==add(scale(-2,L0),L1)
    assert alternate_inverse(alternate_inverse(one))==add(scale(-5,L0),scale(3,L1))
    q=add(v2,scale(-2,v1));L=add(v1,scale(-1,v2))
    assert q==add(L0,scale(-1,L1)) and L==L1
    return {'shift_inverse_tests':count,'actual_U1':v1,'actual_U2':v2,
            'recovered_q':q,'recovered_L':L,
            'alternate_shift_reproduces_printed_tuple':True}


def normalized_mutation_checks():
    """K0(E) rank and full formal Picard exponents, including shifts.

A class is (rank, determinant exponents in L0,L1,p1,...,p6). K0 mutation
uses chi(E,F)=rank(E)*deg(F)-rank(F)*deg(E). Actual cone/sheaf statements
are proved separately by the exact evaluation sequences in the paper.
"""
    degrees=(3,3,1,1,1,1,1,1)
    def degree(x):return sum(a*b for a,b in zip(x[1],degrees))
    def combine(x,y,n):return (x[0]+n*y[0],tuple(a+n*b for a,b in zip(x[1],y[1])))
    def shift(x):return (-x[0],tuple(-a for a in x[1]))
    pts=[(0,tuple(int(j==i+2) for j in range(8))) for i in range(6)]
    U2=(1,(-1,-1,0,0,0,0,0,0)); U1=(1,(-1,0,0,0,0,0,0,0)); O=(1,(0,)*8)
    collection=pts+[U2,U1,O]
    stages=[{'stage':1,'ranks':[x[0] for x in collection],'degrees':[degree(x) for x in collection]}]
    ops=[('L',[1,2,3,4,5,6]),('R_inverse',[5,6,7]),('R_inverse',[6,7,8]),
         ('L',[2,3,4]),('R_inverse',[3,4,5]),('L',[1,2])]
    correction=None
    for stage,(side,comp) in enumerate(ops,start=2):
        for i in reversed(comp):
            E,F=collection[i-1:i+1]
            chi=E[0]*degree(F)-F[0]*degree(E)
            if side=='L':collection[i-1:i+1]=[combine(F,E,-chi),E]
            else:collection[i-1:i+1]=[F,combine(E,F,-chi)]
        if stage==4:
            assert [x[0] for x in collection[6:]]==[-1]*3
            assert [degree(x) for x in collection[6:]]==[-2]*3
            correction={'stage':4,'positions':[7,8,9],'cohomological_shift':1,
                        'ranks_before':[-1,-1,-1],'degrees_before':[-2,-2,-2]}
            collection[6:]=[shift(x) for x in collection[6:]]
        stages.append({'stage':stage,'ranks':[x[0] for x in collection],
                       'degrees':[degree(x) for x in collection]})
    expected=[(0,)*8,(-1,-1,1,1,1,1,1,1),(-1,0,1,1,1,0,0,0)]
    expected += [tuple(int(j==i+2) for j in range(8)) for i in range(3)]
    expected += [tuple(1 if j==0 else -1 if j==i+2 else 0 for j in range(8)) for i in range(3,6)]
    assert [x[1] for x in collection]==expected
    assert [x[0] for x in collection]==[1]*9
    assert [degree(x) for x in collection]==[0]*3+[1]*3+[2]*3
    # Inverse dictionary from the normalized decuple, in the free Picard lattice.
    def plusvec(*vs):return tuple(sum(x) for x in zip(*vs))
    def minusvec(v):return tuple(-a for a in v)
    reconstructed_L0=plusvec(*expected[3:6],minusvec(expected[2]))
    reconstructed_last=[plusvec(reconstructed_L0,minusvec(c)) for c in expected[6:9]]
    reconstructed_D=plusvec(*expected[3:6],*reconstructed_last)
    reconstructed_L1=plusvec(reconstructed_D,minusvec(reconstructed_L0),minusvec(expected[1]))
    assert reconstructed_L0==(1,0,0,0,0,0,0,0)
    assert reconstructed_L1==(0,1,0,0,0,0,0,0)
    assert reconstructed_last==[tuple(int(j==i+2) for j in range(8)) for i in range(3,6)]
    first=expected[2]
    second=tuple(a-b for a,b in zip(expected[1],expected[2]))
    third=expected[1]
    assert second==(0,-1,0,0,0,1,1,1)
    assert all(sum(a*b for a,b in zip(x,degrees))==0 for x in (first,second,third))
    # Explicit Picard substitution L1=O(3o), L0=L1*q, O(p_i)=O(o)*q^Ni.
    # For the fixed non-torsion q this gives actual nonzero exponents;
    # non-torsion and the geometric construction are hypotheses, not tested here.
    values=set();count=0
    for ns in permutations((1,3,2,5,7,11)):
        vals=tuple(x[0]+sum(a*n for a,n in zip(x[2:],ns)) for x in (first,second,third))
        assert all(a>0 for a in vals)
        assert vals==(sum(ns[:3])-1,sum(ns[3:]),sum(ns)-1)
        values.add(vals);count+=1
    return {'exponent_basis':['L0','L1','p1','p2','p3','p4','p5','p6'],
            'stages':stages,'explicit_shift_correction':correction,
            'final_decuple_exponents':expected,
            'inverse_decuple_round_trip':True,
            'inverse_decuple_L0':reconstructed_L0,'inverse_decuple_L1':reconstructed_L1,
            'three_open_conditions_exponents':[first,second,third],
            'integer_configuration_orders_checked':count,
            'integer_configuration_values_count':len(values),
            'full_strongness_or_geometric_existence_proved_by_code':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('build/four_hearts_boundary_checks.json'))
    args=ap.parse_args()
    shift_checks=right_normalized_shift_checks()
    mutation_checks=normalized_mutation_checks()
    rng=Random(20261116)
    matrix_cases=[];nchecks=0
    for r in range(3,9):
        n=r+3;C=[[int(i==j) for j in range(n)] for i in range(n)]
        for i in range(r):
            for j in range(r,n): C[i][j]=-1
        C[r][r+1]=3;C[r][r+2]=6;C[r+1][r+2]=3
        si=multiply(inverse(transpose(C)),C)
        assert all(x.denominator==1 for row in si for x in row)
        si=[[int(x) for x in row] for row in si]
        vv=[[int(i==j) for i in range(n)] for j in range(n)]
        vv += [[rng.randrange(-9,10) for _ in range(n)] for _ in range(256)]
        for v in vv:
            x=numeric_from_basis(v,r)
            sv=[sum(a*b for a,b in zip(row,v)) for row in si]
            sx=numeric_from_basis(sv,r)
            assert sx==tensor_H(x,r)
            assert determinant(sx)==boundary_on_determinant(x,r)
            nchecks+=1
        d=9-r
        point=[0]*r+[1,-2,1]
        assert numeric_from_basis(point,r)==(0,0,*([0]*r),1)
        assert si[-3][-1]==d-3 and si[-2][-1]==3-2*d and si[-1][-1]==d+1
        matrix_cases.append({'blowups':r,'degree':d,'rank_K0':n,
                             'inverse_Serre_structure_column':[row[-1] for row in si]})
        if r==6:
            cubic_si=si;cubic_C=C
    L0=line(3,1);L1=push(-1,L0);L2=push(-2,L0);D=line(6,D=1)
    Q=add(L1,scale(-1,L0))
    U1=add(scale(-2,L0),L1);U2=add(scale(-5,L0),scale(3,L1))
    qres=add(U2,scale(-2,U1));Lres=add(U1,scale(-1,U2))
    assert qres==Q
    Nlit=add(L0,L1,L2,scale(-1,D))
    assert Nlit==add(scale(3,L1),scale(-1,D))
    required_O=add(scale(-3,U1),scale(-1,D))
    literal_O=push(3,Nlit)
    assert literal_O==add(scale(3,L0),scale(-1,D))
    structure_residual=add(required_O,scale(-1,literal_O))
    point_residual=add(Q,scale(-1,line(0,b=3)))
    assert point_residual==scale(2,Q)==line(0,b=-6)
    assert structure_residual==scale(-3,Q)==line(0,b=9)
    # Two independent identities would require Q^2=Q^3=1; hence Q=1.
    assert add(scale(-1,point_residual),scale(-1,structure_residual))==Q
    qb=scale(-1,Q)
    candidates=[]
    for a,b in product(range(3),repeat=2):
        eps=line(0,e1=a,e2=b);L=add(L1,eps)
        v1=add(scale(-1,L0),scale(-1,eps))
        v2=add(scale(-1,L0),scale(-1,L1),scale(-2,eps))
        assert add(v2,scale(-2,v1))==qb
        assert add(v1,scale(-1,v2))==L
        assert add(scale(3,L),scale(-1,D))==Nlit
        assert add(scale(-3,v1),scale(-1,D))==literal_O
        candidates.append({'epsilon':[a,b],'U1':v1,'U2':v2,'L':L})
    assert len({tuple(c['U1']) for c in candidates})==9
    # q=1 (formally b=0) removes the discrepancy, but is not the infinite-order case.
    assert point_residual[1]==point_residual[3]==structure_residual[1]==structure_residual[3]==0
    selected=[c for c in candidates if tuple(c['U1'])==tuple(shift_checks['actual_U1']) and tuple(c['U2'])==tuple(shift_checks['actual_U2'])]
    assert len(selected)==1 and selected[0]['epsilon']==[0,0]
    result={'date':'2026-11-16','version':'hearts-v23','arithmetic':'QQ exact / formal Picard group / (Z/3)^2',
            'K0_cases':matrix_cases,'basis_and_random_vectors_checked':nchecks,
            'cubic_Euler_matrix':cubic_C,'cubic_inverse_Serre':cubic_si,
            'formal_line_coordinates':['degree','AJ_L0','translation_b','D','epsilon1_mod3','epsilon2_mod3'],
            'restriction_recovered_q':qres,'literal_boundary_translation_q':qb,
            'point_residual_required_minus_literal':point_residual,
            'structure_residual_required_minus_literal':structure_residual,
            'literal_common_convention_obstruction':['Q^2=O','Q^3=O','therefore Q=O'],
            'boundary_first_candidates':candidates,'candidate_count':9,
            'right_normalized_shift_checks':shift_checks,
            'normalized_mutation_checks':mutation_checks,
            'unique_candidate_with_actual_plane_twists':selected[0],
            'geometric_dictionary_proved_by_code':False,
            'which_original_formula_requires_relabeling_or_correction_decided':False,
            'scope':'Finite K0/Picard checks, including an explicit normalized mutation procedure. The manuscript proves restriction transport from primary sources. No unedited printed-AOU algebra identification or author-endorsed correction is claimed.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cubic_Euler_matrix','cubic_inverse_Serre','boundary_first_candidates')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
