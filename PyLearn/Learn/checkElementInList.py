m = list(map(int, input("Nhập danh sách số nguyên: ").split()))
index = -1  # Mặc định nếu không tìm thấy
find = False

for i in range(1, len(m) - 1):  # Chỉ xét từ phần tử thứ 1 đến phần tử thứ len(m)-2
    if m[i - 1] * m[i + 1] == m[i]:  # Kiểm tra điều kiện
        index = i  # Gán vị trí thỏa mãn
        find = True
        break

print(index)




