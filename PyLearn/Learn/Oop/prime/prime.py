import math

class prime:
    def __init__(self):
        self.a = []

    def is_prime(self, x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def set_prime(self, x):
        if self.is_prime(x):
            self.a.append(x)

    def get_prime(self):
        return self.a

    def nextPrime(self, x):
        next_num = x + 1
        while True:
            if self.is_prime(next_num):
                return next_num
            next_num += 1  # Tìm số nguyên tố tiếp theo
