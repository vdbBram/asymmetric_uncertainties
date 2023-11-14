import numpy as np
from asyfloat import asyfloat
from asynumpy import asymatrix
import asymath
import asynumpy
x = asyfloat(40,5,20)
k = asymatrix([1,2,3,40],[3,2,2,5],[4,4,5,20])
print(asymath.sin(x), 'x')
print(asynumpy.sin(k), 'k')
from uncertainties import umath
from uncertainties import ufloat as uf
y,z = uf(1,3),uf(1,4)
print(umath.sin(z),umath.sin(y))