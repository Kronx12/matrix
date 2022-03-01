#!/bin/python3
import sys

sys.path.append('../')

from Classes.Matrix import Matrix

# Subject tests:
print("Personal test:")
u = Matrix([[1, 3, 5], [2, 4, 6]])
print("From : " + str(u) + " To : " + str(u.transpose()))

# Corrections tests:
print("Correction tests:")
u = Matrix([[0, 0], [0, 0]])
print("From : " + str(u) + " To : " + str(u.transpose()))

u = Matrix([[1, 0], [0, 1]])
print("From : " + str(u) + " To : " + str(u.transpose()))

u = Matrix([[1, 2], [3, 4]])
print("From : " + str(u) + " To : " + str(u.transpose()))

u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("From : " + str(u) + " To : " + str(u.transpose()))

u = Matrix([[1, 2], [3, 4], [5, 6]])
print("From : " + str(u) + " To : " + str(u.transpose()))
