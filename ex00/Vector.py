class Vector:
    def __init__(self, values_arr):
        if type(values_arr) == list:
            for i in values_arr:
                if type(i) != int and type(i) != float:
                    raise TypeError
        else:
            raise TypeError
        self.values = values_arr

    def __str__(self):
        return "Vector = [" + "".join(list("".join([(str(i) + ", ") for i in self.values]))[:-2]) + "]"

    def shape(self):
        return (len(self.values))

    def add(self, vector):
        if type(vector) != Vector or self.shape() != vector.shape():
            raise TypeError
        for i in range(self.shape()):
            self.values[i] += vector.values[i]

    def sub(self, vector):
        if type(vector) != Vector or self.shape() != vector.shape():
            raise TypeError
        for i in range(self.shape()):
            self.values[i] -= vector.values[i]

    def scl(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError
        for i in range(self.shape()):
            self.values[i] *= scalar
