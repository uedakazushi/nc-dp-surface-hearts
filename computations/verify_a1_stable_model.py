#!/usr/bin/env python3
"""Exact polynomial checks for the A1 stable matrix-factorization model.
Not a proof of complete resolutions, MCM properties, or categorical equivalence."""
import json
import sympy as sp
u,v,w,s,t,z=sp.symbols("u v w s t z")
B=sp.Matrix([[-w,-v],[u,w]])
H=sp.Matrix([[-t,0],[0,-s],[s,t]])
assert B*B==(w*w-u*v)*sp.eye(2)
assert sp.Matrix([[s*s,t*t,s*t]])*H==sp.zeros(1,2)
assert all(H[i,j].subs({s:-s,t:-t})==-H[i,j] for i in range(3) for j in range(2))
assert sp.expand((w*w).subs(w,s*t)-(u*v).subs({u:s*s,v:t*t}))==0
series=sp.expand(sp.series((1+z)**3/(1-z*z),z,0,12).removeO())
coeff=[int(series.coeff(z,n)) for n in range(11)]
assert coeff[:2]==[1,3] and all(x==4 for x in coeff[2:])
print(json.dumps({"status":"PASS","matrix_square":"(w^2-u*v)I",
"hilbert_burch_relations":True,"odd_coefficients":True,
"poincare_coefficients":coeff,
"scope":"Symbolic checks only; full algebraic proofs remain in the manuscript."},indent=2))
