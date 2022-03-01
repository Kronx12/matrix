#!/bin/python3

from Matrix import Matrix

# Subject tests:
print("Subject tests:")
u = Matrix([[1., 0.], [0., 1.]])
print(u.trace())

u = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
print(u.trace())

u = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
print(u.trace())

# Corrections tests:
print("Correction tests:")
u = Matrix([[0., 0.], [0., 0.]])
print(u.trace())

u = Matrix([[1., 0.], [0., 1.]])
print(u.trace())

u = Matrix([[1., 2.], [3., 4.]])
print(u.trace())

u = Matrix([[8., -7.], [4., 2.]])
print(u.trace())

u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(u.trace())
