import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        """Đơn giản hóa phân số"""
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def reversed(self):
        if self.numerator == 0:
            raise ValueError("Cannot reverse a fraction with numerator 0")
        return f"{self.denominator}/{self.numerator}"

    @staticmethod
    def inputListFraction(n):
        """Nhập danh sách n phân số"""
        fractions = []
        for i in range(n):
            num = int(input(f"Nhập tử số phân số {i + 1}: "))
            denom = int(input(f"Nhập mẫu số phân số {i + 1} (≠ 0): "))
            fractions.append(Fraction(num, denom))
        return fractions

    @staticmethod
    def showFraction(fractions):
        """Hiển thị danh sách phân số"""
        for i, frac in enumerate(fractions, 1):
            print(f"Phân số {i}: {frac}", end="  ")
        print()

    @staticmethod
    def reversedList(fractions):
        """Hiển thị danh sách phân số nghịch đảo"""
        for i, frac in enumerate(fractions, 1):
            try:
                print(f"Nghịch đảo phân số {i}: {frac.reversed()}", end="  ")
            except ValueError as e:
                print(f"Nghịch đảo phân số {i}: ERROR ({e})", end="  ")
        print()  # Xuống dòng sau khi in xong

    @staticmethod
    def addFractions(fractions):
        """Cộng tất cả phân số trong danh sách"""
        result = fractions[0]
        for frac in fractions[1:]:
            result = Fraction(result.numerator * frac.denominator + result.denominator * frac.numerator,
                              result.denominator * frac.denominator)
            result.simplify()
        print(f"Tổng các phân số: {result}")

    @staticmethod
    def subFractions(fractions):
        """Trừ tất cả phân số trong danh sách"""
        result = fractions[0]
        for frac in fractions[1:]:
            result = Fraction(result.numerator * frac.denominator - result.denominator * frac.numerator,
                              result.denominator * frac.denominator)
            result.simplify()
        print(f"Hiệu các phân số: {result}")

    @staticmethod
    def mulFractions(fractions):
        """Nhân tất cả phân số trong danh sách"""
        result = fractions[0]
        for frac in fractions[1:]:
            result = Fraction(result.numerator * frac.numerator, result.denominator * frac.denominator)
            result.simplify()
        print(f"Tích các phân số: {result}")

    @staticmethod
    def divFractions(fractions):
        """Chia tất cả phân số trong danh sách"""
        result = fractions[0]
        for frac in fractions[1:]:
            if frac.numerator == 0:
                print("Lỗi: Không thể chia cho phân số có tử số bằng 0")
                return
            result = Fraction(result.numerator * frac.denominator, result.denominator * frac.numerator)
            result.simplify()
        print(f"Thương các phân số: {result}")