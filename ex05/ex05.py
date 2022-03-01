#!/bin/python3
import sys

sys.path.append('../')

from Classes.Vector import Vector

def angle_cos(vector_a, vector_b):
    if type(vector_a) != Vector or type(vector_b) != Vector:
        raise TypeError
    return vector_a.dot(vector_b)/(vector_a.norm() * vector_b.norm())

# Subject tests:
print("Subject tests:")
u = Vector([1., 0.])
v = Vector([1., 0.])
print(angle_cos(u, v))

u = Vector([1., 0.])
v = Vector([0., 1.])
print(angle_cos(u, v))

u = Vector([-1., 1.])
v = Vector([1., -1.])
print(angle_cos(u, v))

u = Vector([2., 1.])
v = Vector([4., 2.])
print(angle_cos(u, v))

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(angle_cos(u, v))

# Corrections tests:
print("Correction tests:")

u = Vector([1., 0.])
v = Vector([0., 1.])
print(angle_cos(u, v))

u = Vector([8., 7.])
v = Vector([3., 2.])
print(angle_cos(u, v))

u = Vector([1., 1.])
v = Vector([1., 1.])
print(angle_cos(u, v))

u = Vector([4., 2.])
v = Vector([1., 1.])
print(angle_cos(u, v))

u = Vector([-7., 3.])
v = Vector([6., 4.])
print(angle_cos(u, v))
print(angle_cos(v, u))
