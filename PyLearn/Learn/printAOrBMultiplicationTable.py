def in_bang_cuu_chuong(a, b):
    # Sử dụng biểu thức điều kiện để tìm số lớn hơn
    n = a if a > b else b

    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 11):  # Lặp từ 1 đến 10
        print(f"{n} x {i} = {n * i}")

# Nhập 2 số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

# Gọi hàm
in_bang_cuu_chuong(a, b)
