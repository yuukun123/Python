from shapes import shapes

class triangle(shapes):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def show_area_and_perimeter(self):
        print(f"Dien tich: {self.calculate_area():.2f}")
        print(f"Chu vi: {self.calculate_perimeter():.2f}")
