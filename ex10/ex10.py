#!/bin/python3
import sys

sys.path.append('../')

from Classes.Matrix import Matrix

# Subject tests:
print("Subject test:")
u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[1, 2], [3, 4]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[1, 2], [2, 4]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[8., 5., -2., 4., 28.], [8., 5., 1., 4., 17.], [3., 2.5, 20., 4., -4.]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

# Corrections tests:
print("Correction tests:")
u = Matrix([[0, 0], [0, 0]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[1, 0], [0, 1]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[4, 2], [2, 1]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[-7, 2], [4, 8]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))

u = Matrix([[1, 2], [4, 8]])
print("From : " + str(u) + " To : " + str(u.row_echelon()))
