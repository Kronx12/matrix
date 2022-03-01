from Vector import Vector

class Matrix:
    def __init__(self, values_arr):
        if type(values_arr) == list and len(values_arr) > 0:
            last = len(values_arr[0])
            for i in values_arr:
                if len(i) != last:
                    raise TypeError("Inequals lines length")
                if type(i) == list:
                    for j in i:
                        if type(j) != int and type(j) != float:
                            raise TypeError
                else:
                    raise TypeError
        else:
            raise TypeError
        self.values = values_arr

    def __str__(self):
        return "Matrix = [\n" + "".join(("   [" + "".join(list("".join([(str(j) + ", ") for j in i]))[:-2]) + "]\n") for i in self.values) + "]"

    def shape(self):
        return (len(self.values), len(self.values[0]))

    def add(self, matrix):
        if type(matrix) != Matrix or self.shape() != matrix.shape():
            raise TypeError
        for i in range(self.shape()[0]):
            for j in range(self.shape()[1]):
                self.values[i][j] += matrix.values[i][j]

    def sub(self, matrix):
        if type(matrix) != Matrix or self.shape() != matrix.shape():
            raise TypeError
        for i in range(self.shape()[0]):
            for j in range(self.shape()[1]):
                self.values[i][j] -= matrix.values[i][j]

    def scl(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError
        for i in range(self.shape()[0]):
            for j in range(self.shape()[1]):
                self.values[i][j] *= scalar

    def mul_vec(self, vector):
        if type(vector) != Vector or self.shape()[1] != vector.shape():
            raise TypeError
        result = []
        for i in self.values:
            tmp = 0
            for j in range(len(i)):
                tmp += i[j] * vector.values[j]
            result.append(tmp)
        return Vector(result)

    def mul_mat(self, matrix):
        if type(matrix) != Matrix or self.shape()[0] != matrix.shape()[1] or self.shape()[1] != matrix.shape()[0]:
            raise TypeError
        result = []
        for i in range(self.shape()[0]):
            row = []
            for j in range(self.shape()[0]):
                tmp = 0
                for k in range(self.shape()[1]):
                    tmp += self.values[i][k] * matrix.values[k][j]
                row.append(tmp)
            result.append(row)
        return Matrix(result)