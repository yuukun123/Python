class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def inputComplex(self):
        self.real = float(input("Nhap phan thuc: "))
        self.imaginary = float(input("Nhap phan ao: "))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / denominator, (self.imaginary * other.real - self.real * other.imaginary) / denominator)