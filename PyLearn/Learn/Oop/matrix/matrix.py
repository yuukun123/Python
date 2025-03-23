class Matrix:
    def __init__(self, matrix):
        if not all(isinstance(row , list) for row in matrix):
            raise TypeError("Matrix must be a list of lists")
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    @staticmethod
    def inputMaxtrix(rows, cols):
        matrix = []
        for i in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols:
                raise ValueError("Matrix must be a list of lists")
            matrix.append(row)
        return Matrix(matrix)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have the same dimensions")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)