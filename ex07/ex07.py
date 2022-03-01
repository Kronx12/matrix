#!/bin/python3

from Vector import Vector
from Matrix import Matrix

# Subject tests:
print("Subject tests:")
u = Matrix([[1., 0.], [0., 1.]])
v = Vector([4., 2.])
print(u.mul_vec(v))

u = Matrix([[2., 0.], [0., 2.]])
v = Vector([4., 2.])
print(u.mul_vec(v))

u = Matrix([[2., -2.], [-2., 2.]])
v = Vector([4., 2.])
print(u.mul_vec(v))

u = Matrix([[1., 0.], [0., 1.]])
v = Matrix([[1., 0.], [0., 1.]])
print(u.mul_mat(v))

u = Matrix([[1., 0.], [0., 1.]])
v = Matrix([[2., 1.], [4., 2.]])
print(u.mul_mat(v))

u = Matrix([[3., -5.], [6., 8.]])
v = Matrix([[2., 1.], [4., 2.]])
print(u.mul_mat(v))

u = Matrix([[1., 0.], [2., -1.]])
v = Matrix([[3., 4.], [-2., -3.]])
print(u.mul_mat(v))

u = Matrix([[1., 2., 0.], [4., 3., -1.]])
v = Matrix([[5., 1.], [2., 3.], [3., 4.]])
print(u.mul_mat(v))

u = Matrix([[5., 1.], [2., 3.], [3., 4.]])
v = Matrix([[1., 2., 0.], [4., 3., -1.]])
print(u.mul_mat(v))

# Corrections tests:
print("Correction tests:")

u = Matrix([[0, 0], [0, 0]])
v = Vector([4, 2])
print(u.mul_vec(v))

u = Matrix([[1, 0], [0, 1]])
v = Vector([4, 2])
print(u.mul_vec(v))

u = Matrix([[1, 1], [1, 1]])
v = Vector([4, 2])
print(u.mul_vec(v))

u = Matrix([[2, 0], [0, 2]])
v = Vector([2, 1])
print(u.mul_vec(v))

u = Matrix([[0.5, 0], [0, 0.5]])
v = Vector([4, 2])
print(u.mul_vec(v))