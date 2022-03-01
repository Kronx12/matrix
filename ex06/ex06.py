#!/bin/python3

from Vector import Vector

def cross_product(vector_a, vector_b):
    if type(vector_a) != Vector or type(vector_b) != Vector or vector_a.shape() != 3 or vector_b.shape() != 3:
        raise TypeError
    result = []
    result.append(vector_a.values[1] * vector_b.values[2] - vector_a.values[2] * vector_b.values[1])
    result.append(vector_a.values[2] * vector_b.values[0] - vector_a.values[0] * vector_b.values[2])
    result.append(vector_a.values[0] * vector_b.values[1] - vector_a.values[1] * vector_b.values[0])
    return Vector(result)

# Subject tests:
print("Subject tests:")
u = Vector([0., 0., 1.])
v = Vector([1., 0., 0.])
print(cross_product(u, v))

u = Vector([1., 2., 3.])
v = Vector([4., 5., 6.])
print(cross_product(u, v))

u = Vector([4., 2., -3.])
v = Vector([-2., -5., 16.])
print(cross_product(u, v))

# Corrections tests:
print("Correction tests:")

u = Vector([0, 0, 0])
v = Vector([0, 0, 0])
print(cross_product(u, v))

u = Vector([1, 0, 0])
v = Vector([0, 0, 0])
print(cross_product(u, v))

u = Vector([1, 0, 0])
v = Vector([0, 1, 0])
print(cross_product(u, v))

u = Vector([8, 7, -4])
v = Vector([3, 2, 1])
print(cross_product(u, v))

u = Vector([1, 1, 1])
v = Vector([0, 0, 0])
print(cross_product(u, v))

u = Vector([1, 1, 1])
v = Vector([1, 1, 1])
print(cross_product(u, v))