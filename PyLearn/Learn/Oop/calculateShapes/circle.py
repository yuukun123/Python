from shapes import shapes
from math import pi

class circle(shapes):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius

    def show_area_and_perimeter(self):
        print(f"Dien tich: {self.calculate_area():.2f}")
        print(f"Chu vi: {self.calculate_perimeter():.2f}")
