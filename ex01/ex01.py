#!/usr/local/bin/python3
import sys

sys.path.append('../')

from Classes.Matrix import Matrix
from Classes.Vector import Vector

def linear_combination(values_list, scalar_list):
    if type(values_list) != list or type(scalar_list) != list:
        raise TypeError
    for i in scalar_list:
        if type(i) != int and type(i) != float:
            raise TypeError
    if type(values_list[0]) == Vector:
        for i in values_list:
            if type(i) != Vector:
                raise TypeError
    elif type(values_list[0]) == Matrix:
        for i in values_list:
            if type(i) != Matrix:
                raise TypeError
    else:
        raise TypeError
    if len(values_list) != len(scalar_list):
        raise TypeError
    arr = []
    for i in range(len(values_list)):
        # Perform deepcopy for Vector or Matrix
        arr.append(type(values_list[i])(values_list[i].values.copy()))
        arr[i].scl(scalar_list[i])
    for i in range(1, len(arr)):
        arr[0].add(arr[i]) 
    return arr[0]

# Subject tests:
print("Subject tests:")

e1 = Vector([1., 0., 0.])
e2 = Vector([0., 1., 0.])
e3 = Vector([0., 0., 1.])
print(linear_combination([e1, e2, e3], [10., -2., 0.5]))

v1 = Vector([1., 2., 3.])
v2 = Vector([0., 10., -100.])
print(linear_combination([v1, v2], [10., -2.]))

# Corrections tests:
print("Correction tests:")

print(linear_combination([Vector([-42., 42.])], [-1.]))
print(linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.]))
print(linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.]))
print(linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.]))
print(linear_combination([Matrix([[-42., 42.]])], [-1.]))
print(linear_combination([Matrix([[-42.]]), Matrix([[-42.]]), Matrix([[-42.]])], [-1., 1., 0.]))
print(linear_combination([Matrix([[-42., 42.], [420., -420.]]), Matrix([[1., 3.], [2., 4.]]), Matrix([[10., 20.], [30., 40.]])], [1., -10., -1.]))
