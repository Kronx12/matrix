#!/usr/local/bin/python3
import sys

sys.path.append('../')

from Classes.Vector import Vector

# Subject tests:
print("Subject tests:")
u = Vector([0., 0.])
v = Vector([1., 1.])
print(u.dot(v))

u = Vector([1., 1.])
v = Vector([1., 1.])
print(u.dot(v))

u = Vector([-1., 6.])
v = Vector([3., 2.])
print(u.dot(v))

# Corrections tests:
print("Correction tests:")
u = Vector([0., 0.])
v = Vector([0., 0.])
print(u.dot(v))

u = Vector([1., 0.])
v = Vector([0., 0.])
print(u.dot(v))

u = Vector([1., 0.])
v = Vector([1., 0.])
print(u.dot(v))

u = Vector([1., 0.])
v = Vector([0., 1.])
print(u.dot(v))

u = Vector([1., 1.])
v = Vector([1., 1.])
print(u.dot(v))

u = Vector([4., 2.])
v = Vector([2., 1.])
print(u.dot(v))