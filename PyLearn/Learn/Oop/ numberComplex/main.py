from complex import Complex

if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(4, 5)

    print(c1)
    print(c2)

    # trong python __add__ cơ bản là c1 + c2 và có thể thay thế bằng dấu +
    # nên không cần câu lenh c1.__add__(c2) mà chỉ cần đơn giản c1 + c2

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    result = c1 / c2
    print(f"{result.real:.2f} + {result.imaginary:.2f}i")