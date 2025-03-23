from vector import Vector

if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(1, 2)
    # print(v)
    print(v1.__eq__(v2))
    print(v1.calculate_angle(v2))
    print(v1.checkTwoVectorIsSameDirection(v2))
    print(v1.__add__(v2))
    print(v1.__sub__(v2))
    print(v1.__mul__(v2))