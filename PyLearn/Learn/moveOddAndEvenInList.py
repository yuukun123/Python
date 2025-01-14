m = list(map(int, input("Nhập danh sách số nguyên: ").split()))

# Tách các phần tử thành 3 danh sách
even = [x for x in m if x != 0 and x % 2 == 0]  # Số chẵn (khác 0)
zero = [x for x in m if x == 0]                 # Số 0
odd = [x for x in m if x % 2 != 0]              # Số lẻ

# Ghép lại danh sách theo thứ tự yêu cầu
result = even + zero + odd

print("Danh sách sau khi sắp xếp:", result)
