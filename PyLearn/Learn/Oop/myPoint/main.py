from myCircle import myCircle
from myPoint import myPoint

if __name__ == "__main__":
    p1 = myPoint(3, 0)
    p2 = myPoint(0, 4)
    print(p1.__str__())
    print(p2.__str__())
    print()
    print(p1.distancePoint(p2))
    print(p1.distance(5,6))
    print()

    Circle = myCircle()
    Circle.TestMyCircle()