#!/usr/bin/env python3
"""Exact root-chamber checks for the anticanonical heart selection theorem.

Only integer arithmetic and the Python standard library are used. The finite
checks verify root combinatorics, not existence of sheaves, derived functors,
or t-structures. The E6 spectrum requires the manuscript's explicit existence
hypotheses. Run from the bundle/repository root.
"""
from __future__ import annotations
import argparse
from collections import deque
import json
from pathlib import Path
from random import Random


def pairing(x: tuple[int, ...], y: tuple[int, ...], edges: list[tuple[int,int]]) -> int:
    """Positive Cartan pairing; geometric intersection has the opposite sign."""
    return 2*sum(a*b for a,b in zip(x,y))-sum(x[i]*y[j]+x[j]*y[i] for i,j in edges)


def reflect(x: tuple[int, ...], j: int, edges: list[tuple[int,int]]) -> tuple[int, ...]:
    y=list(x)
    y[j] -= 2*x[j]-sum(x[b] if a==j else x[a] if b==j else 0 for a,b in edges)
    return tuple(y)


def roots(rank: int, edges: list[tuple[int,int]]) -> set[tuple[int, ...]]:
    initial=[tuple(int(i==j) for i in range(rank)) for j in range(rank)]
    seen=set(initial); queue=deque(initial)
    while queue:
        x=queue.popleft()
        for j in range(rank):
            y=reflect(x,j,edges)
            if y not in seen:
                seen.add(y);queue.append(y)
    assert all(pairing(x,x,edges)==2 for x in seen)
    assert all(all(a>=0 for a in x) or all(a<=0 for a in x) for x in seen)
    return seen


def value(m: tuple[int, ...], x: tuple[int, ...]) -> int:
    return sum(a*b for a,b in zip(m,x))


def chamber(m: tuple[int, ...], rr: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    positive={x for x in rr if value(m,x)>0}
    # A positive root is simple precisely when not a sum of two positive roots.
    return {x for x in positive if not any(tuple(a-b for a,b in zip(x,y)) in positive for y in positive)}


def run_algorithm(m: tuple[int, ...], edges: list[tuple[int,int]], rr: set[tuple[int, ...]], strategy: int):
    r=len(m); basis=[tuple(int(i==j) for i in range(r)) for j in range(r)]
    original_positive={x for x in rr if all(a>=0 for a in x)}
    count=sum(value(m,x)<0 for x in original_positive)
    sequence=[]
    while True:
        vals=[value(m,x) for x in basis]
        assert all(vals), 'A zero simple is outside the assumed positive-target setting.'
        bad=[j for j in range(r) if vals[j]<0]
        if not bad:break
        j=min(bad) if strategy==0 else max(bad) if strategy==1 else min(bad,key=lambda j:(vals[j],j))
        old=basis[j]
        for a,b in edges:
            if j in (a,b):
                i=b if a==j else a
                basis[i]=tuple(x+y for x,y in zip(basis[i],old))
        basis[j]=tuple(-x for x in old)
        assert all(x in rr for x in basis)
        sequence.append(j)
        assert len(sequence)<=count, 'Negative-positive-root count must decrease at every step.'
    assert len(sequence)==count
    assert len(set(basis))==r
    for i in range(r):
        for j in range(r):
            assert pairing(basis[i],basis[j],edges)==(2 if i==j else -1 if (min(i,j),max(i,j)) in edges else 0)
    return sequence,basis,[value(m,x) for x in basis]


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('build/four_hearts_chamber_checks.json'))
    parser.add_argument('--samples',type=int,default=32)
    args=parser.parse_args()
    if args.samples<1:raise ValueError('--samples must be positive')
    rng=Random(20261116)
    types=[]
    expected={3:8,4:20,5:40,6:72,7:126,8:240}
    names={3:'A2+A1',4:'A4',5:'D5',6:'E6',7:'E7',8:'E8'}
    for r in range(3,9):
        edges=([(0,3)] if r>=4 else [])+[(i,i+1) for i in range(1,r-1)]
        rr=roots(r,edges); assert len(rr)==expected[r]
        max_steps=0; counts=[]
        for sample in range(args.samples):
            # A positive functional is regular; reflected functionals stay regular.
            m=[rng.randint(1,19) for _ in range(r)]
            for _ in range(rng.randint(0,5*r*r)):
                j=rng.randrange(r); old=m[j]
                for a,b in edges:
                    if j in (a,b):m[b if a==j else a]+=old
                m[j]=-old
            m=tuple(m)
            assert all(value(m,x)!=0 for x in rr)
            expected_basis=chamber(m,rr)
            assert len(expected_basis)==r
            for strategy in range(3):
                seq,basis,vals=run_algorithm(m,edges,rr,strategy)
                assert set(basis)==expected_basis
                max_steps=max(max_steps,len(seq))
            counts.append(len(seq))
        types.append({'type':names[r],'rank':r,'roots':len(rr),
                      'regular_functionals':args.samples,'strategies_per_functional':3,
                      'maximum_reflection_length_seen':max_steps,
                      'all_terminal_bases_match_positive_root_chamber':True})
        if r==6:
            e6_roots=rr;e6_edges=edges
    m=(6,2,-1,3,2,4)
    seq,basis,vals=run_algorithm(m,e6_edges,e6_roots,0)
    assert seq==[2] and vals==[6,1,1,2,2,4]
    assert len(chamber(m,e6_roots))==6
    result={
        'date':'2026-11-16','version':'hearts-v20','arithmetic':'exact integers',
        'types':types,'total_regular_functionals':6*args.samples,
        'total_reflection_runs':18*args.samples,
        'E6_example':{'edges':e6_edges,'old_Euler_values':m,'reflection_sequence':seq,
                      'new_simple_root_columns':basis,'new_Euler_values':vals,
                      'negative_initial_positive_roots':1,'one_dimensional_simples_if_realized':2},
        'geometric_existence_verified_by_this_code':False,
        'derived_equivalence_or_heart_equality_proved_by_this_code':False,
        'scope':'Finite exact checks of the root algorithm. Categorical arguments and actual-root existence assumptions are in the manuscript.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
