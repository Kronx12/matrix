#!/usr/local/bin/python3
import sys

sys.path.append('../')

from Classes.Matrix import Matrix

# Subject tests:
print("Subject test:")
u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(u.inverse())

u = Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])
print(u.inverse())

u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
print(u.inverse())

# Corrections tests:
print("Correction tests:")
u = Matrix([[1, 0], [0, 1]])
print(u.inverse())

u = Matrix([[2, 0], [0, 2]])
print(u.inverse())

u = Matrix([[0.5, 0], [0, 0.5]])
print(u.inverse())

u = Matrix([[0, 1], [1, 0]])
print(u.inverse())

u = Matrix([[1, 2], [3, 4]])
print(u.inverse())

u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(u.inverse())
