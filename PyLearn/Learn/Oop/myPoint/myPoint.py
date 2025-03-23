from math import sqrt

class myPoint:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, x, y):
        return sqrt((self.x - x)**2 + (self.y - y)**2)

    def distancePoint(self, point1):
        return sqrt((self.x - point1.x)**2 + (self.y - point1.y)**2)