import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def calculate_angle(self, other):
        # vector a(xa, ya) vector b (xa, ya)
        # tìm góc θ = arccos( (a.b)/ (|a|.|b|) )
        # |a| = sqrt(xa**2 + ya**2), |b| = sqrt(xb**2 + yb**2)
        dot_product = self.x * other.x + self.y * other.y # xa * xb + ya * yb
        mag_a = math.sqrt(self.x ** 2 + self.y ** 2)
        mag_b = math.sqrt(other.x ** 2 + other.y ** 2)
        magnitude = mag_a * mag_b # |a| * |b| = sqrt(xa**2 + ya**2) * sqrt(xb**2 + yb**2)
        if mag_a == 0 or mag_b == 0:
            raise ValueError("can't calculate with angle = 0")
        cos_theta = dot_product / magnitude
        cos_theta = max(min(cos_theta, 1.0), -1.0)
        return math.degrees(math.acos(cos_theta)) # Converts an angle from radians to degrees

    def checkTwoVectorIsSameDirection(self, other):
        # ax / bx = ay / by

        if (self.x == 0 and self.y == 0) or (other.x == 0 and other.y == 0):
            return (self.x == other.x) and (self.y == other.y)

        if other.x == 0:
            if self.x != 0:
                return False # nếu bx = 0 mà ax != 0 thì trả về false
            if other.y != 0: # nếu bx = 0 nhưng by != 0 thì thực hiện tính k
                return self.y / other.y > 0
            else:
                return True

        if other.y == 0:
            if self.y != 0:
                return False # khi
            if other.x != 0:
                return self.x / other.x > 0
            else:
                return True

        if self.x / other.x == self.y / other.y:
            return self.x * other.x > 0 # kiểm tra xem k có cùng hướng hay ngược hướng
        return False

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector): # nhân với vector
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)): # nhân với số nguyên hoặc số thực
            return Vector(self.x * other, self.y * other)
        raise TypeError("Chỉ nhân được với Vector hoặc số")