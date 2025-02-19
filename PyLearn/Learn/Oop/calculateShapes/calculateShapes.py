from circle import circle
from rectangle import rectangle
from triangle import triangle

if __name__ == "__main__":
    radius = float(input("Nhap ban kinh hinh tron: "))
    circle1 = circle(radius)
    circle1.show_area_and_perimeter()

    width = float(input("Nhap chieu dai hinh chu nhat: "))
    height = float(input("Nhap chieu rong hinh chu nhat: "))
    rectangle1 = rectangle(width, height)
    rectangle1.show_area_and_perimeter()

    base = float(input("Nhap chieu dai day hinh tam giac: "))
    height = float(input("Nhap chieu cao hinh tam giac: "))
    side_a = float(input("Nhap do dai canh a: "))
    side_b = float(input("Nhap do dai canh b: "))
    side_c = float(input("Nhap do dai canh c: "))
    triangle1 = triangle(base, height, side_a, side_b, side_c)
    triangle1.show_area_and_perimeter()