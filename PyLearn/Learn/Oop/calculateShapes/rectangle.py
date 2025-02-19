from shapes import shapes

class rectangle(shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def show_area_and_perimeter(self):
        print(f"Dien tich: {self.calculate_area():.2f}")
        print(f"Chu vi: {self.calculate_perimeter():.2f}")
