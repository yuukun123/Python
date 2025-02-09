from math import sqrt

def distance(x, y):
    # tính khoảng cách giữa hai điềm
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def is_valid_triangle(a, b, c):
    """Kiểm tra điều kiện tạo thành tam giác"""
    return a + b > c and a + c > b and b + c > a

def isoscelesTriangle():
    try:
        with open("tgcan.inp", "r") as fr, open("tgcan.out", "w") as fw:
            size = int(fr.readline().strip())
            points = [tuple(map(int, line.strip().split())) for line in fr.readlines()]

            if len(points) != size:
                print("Invalid input")
                return

            count_isoscelesTriangle = 0

            for i in range(size - 2):
                for j in range(i + 1, size - 1):
                    for k in range(j + 1, size):
                        A, B, C = points[i], points[j], points[k]

                        AB, AC, BC = distance(A, B), distance(A, C), distance(B, C)

                        if is_valid_triangle(AB, AC, BC) and (AB == AC or AB == BC or AC == BC):
                            count_isoscelesTriangle += 1

            print(count_isoscelesTriangle)
            fw.write(str(count_isoscelesTriangle) + "\n")

            print(points)

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid input")

isoscelesTriangle()