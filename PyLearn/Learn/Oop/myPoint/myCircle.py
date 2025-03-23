from math import pi
from myPoint import myPoint


class myCircle(myPoint):
    def __init__(self, center = myPoint(), radius = 0):
        self.center = center
        self.radius = radius

    def getRadius(self, ):
        return self.radius

    def setRadius(self, radius):
        if radius >0:
            self.radius = radius

    def setCenter(self, center):
        self.center = center

    def getCenter(self):
        return self.center

    def getArea(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"({self.center.__str__()}, {self.radius})"

    def TestMyCircle(self):
        # Test Case 1: Tạo một đường tròn với tâm (0, 0) và bán kính 3
        center1 = myPoint(0, 0)
        circle1 = myCircle(center1, 3)
        print(f"Thông tin đường tròn 1: {circle1.__str__()}")
        print(f"Diện tích đường tròn 1: {circle1.getArea():.2f}")

        # Test Case 2: Thay đổi tâm và bán kính
        center2 = myPoint(1, 2)
        circle1.setCenter(center2)
        circle1.setRadius(5)
        print(f"Thông tin đường tròn 1 sau khi thay đổi: {circle1.__str__()}")
        print(f"Diện tích đường tròn 1 sau khi thay đổi: {circle1.getArea():.2f}")

        # Test Case 3: Tạo một đường tròn khác với tâm (3, 4) và bán kính 2
        center3 = myPoint(3, 4)
        circle2 = myCircle(center3, 2)
        print(f"Thông tin đường tròn 2: {circle2.__str__()}")
        print(f"Diện tích đường tròn 2: {circle2.getArea():.2f}")