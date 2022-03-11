#!/usr/local/bin/python3
import sys

sys.path.append('../')

from Classes.Matrix import Matrix
import math

def projection(fov, ratio, near, far):
    return Matrix([[(1 / (math.tan(fov / 2))) / ratio, 0, 0, 0],
                    [0, 1 / math.tan(fov / 2), 0, 0],
                    [0, 0, (near + far) / (near - far), (2 * far * near) / (near - far)],
                    [0, 0, -1, 0]])

def output_matrix(m):
    s = ""
    for i in m.values:
        for j in i:
            s += str(j) + ", "
        s = s[:-2] + '\n'
    s = s[:-1]
    print(s)
    f = open("./proj", "w")
    f.write(s)
    f.close()

result = projection(math.radians(70), 1, 1, 100)
output_matrix(result)