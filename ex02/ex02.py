#!/bin/python3
import sys

sys.path.append('../')

from Classes.Vector import Vector
from Classes.Matrix import Matrix

def lerp(value_a, value_b, scalar):
    if type(value_a) != type(value_b) or (type(value_a) != int and type(value_a) != float and type(value_a) != Vector and type(value_a) != Matrix):
        raise TypeError
    
    if type(value_a) == Vector or type(value_a) == Matrix:
        cp = type(value_b)(value_b.values.copy())
        cp.sub(value_a)
        cp.scl(scalar)
        cp.add(value_a)
        return cp
    else:
        return (value_b - value_a) * scalar + value_a

# Subject tests:
print("Subject tests:")

print(lerp(0., 1., 0.))
print(lerp(0., 1., 1.))
print(lerp(0., 1., 0.5))
print(lerp(21., 42., 0.3))

print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))

# Corrections tests:
print("Correction tests:")
print(lerp(0., 42., 0.5))
print(lerp(-42., 42., 0.5))
print(lerp(Vector([-42., 42.]), Vector([42., -42.]), 0.5))