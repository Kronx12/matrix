#!/bin/python3

from Vector import Vector
from Matrix import Matrix

# Subject exemples:
print("Subject tests:")

u = Vector([2., 3.])
v = Vector([5., 7.])
u.add(v)
print(u)

u = Vector([2., 3.])
v = Vector([5., 7.])
u.sub(v)
print(u)

u = Vector([2., 3.])
u.scl(2.)
print(u)

u = Matrix([[1., 2.], [3., 4.]])
v = Matrix([[7., 4.], [-2., 2.]])
u.add(v)
print(u)

u = Matrix([[1., 2.], [3., 4.]])
v = Matrix([[7., 4.], [-2., 2.]])
u.sub(v)
print(u)

u = Matrix([[1., 2.], [3., 4.]])
u.scl(2.)
print(u)

# Corrections exemples:

# Add
print("Addition tests:")

u = Vector([0, 0])
v = Vector([0, 0])
u.add(v)
print(u)

u = Vector([1, 0])
v = Vector([0, 1])
u.add(v)
print(u)

u = Vector([1, 1])
v = Vector([1, 1])
u.add(v)
print(u)

u = Vector([21, 21])
v = Vector([21, 21])
u.add(v)
print(u)

u = Vector([-21, 21])
v = Vector([21, -21])
u.add(v)
print(u)

u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
u.add(v)
print(u)

u = Matrix([[0, 0], [0, 0]])
v = Matrix([[0, 0], [0, 0]])
u.add(v)
print(u)

u = Matrix([[1, 0], [0, 1]])
v = Matrix([[0, 0], [0, 0]])
u.add(v)
print(u)

u = Matrix([[1, 1], [1, 1]])
v = Matrix([[1, 1], [1, 1]])
u.add(v)
print(u)

u = Matrix([[21, 21], [21, 21]])
v = Matrix([[21, 21], [21, 21]])
u.add(v)
print(u)

# Sub
print("Substract tests:")

u = Vector([0, 0])
v = Vector([0, 0])
u.sub(v)
print(u)

u = Vector([1, 0])
v = Vector([0, 1])
u.sub(v)
print(u)

u = Vector([1, 1])
v = Vector([1, 1])
u.sub(v)
print(u)

u = Vector([21, 21])
v = Vector([21, 21])
u.sub(v)
print(u)

u = Vector([-21, 21])
v = Vector([21, -21])
u.sub(v)
print(u)

u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
u.sub(v)
print(u)

u = Matrix([[0, 0], [0, 0]])
v = Matrix([[0, 0], [0, 0]])
u.sub(v)
print(u)

u = Matrix([[1, 0], [0, 1]])
v = Matrix([[0, 0], [0, 0]])
u.sub(v)
print(u)

u = Matrix([[1, 1], [1, 1]])
v = Matrix([[1, 1], [1, 1]])
u.sub(v)
print(u)

u = Matrix([[21, 21], [21, 21]])
v = Matrix([[21, 21], [21, 21]])
u.sub(v)
print(u)


# Scl
print("Scalar tests:")

u = Vector([0, 0])
u.scl(1)
print(u)

u = Vector([1, 0])
u.scl(1)
print(u)

u = Vector([1, 1])
u.scl(2)
print(u)

u = Vector([42, 42])
u.scl(2)
print(u)

u = Vector([21, 21])
u.scl(0.5)
print(u)

u = Matrix([[0, 0], [0, 0]])
u.scl(0)
print(u)

u = Matrix([[1, 0], [0, 1]])
u.scl(1)
print(u)

u = Matrix([[1, 2], [3, 4]])
u.scl(2)
print(u)

u = Matrix([[21, 21], [21, 21]])
u.scl(0.5)
print(u)