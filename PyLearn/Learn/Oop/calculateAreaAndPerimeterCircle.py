from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self): # tính diện tích hình tròn
        return pi * self.radius ** 2

    def calculate_perimeter(self): # tính chu vi hình tròn
        return 2 * pi * self.radius

    def show_area_and_perimeter(self): # hien thi thong tin hinh tron
        print(f"Dien tich: {self.calculate_area():.2f}")
        print(f"Chu vi: {self.calculate_perimeter():.2f}")


radisu = float(input("Nhap ban kinh hinh tron: "))
circle = Circle(radisu)
circle.show_area_and_perimeter()

