a = "Xin chào mọi người!"
b = "Xin chào"

wordA = a.split()
wordB = b.split()
result = []

# Tạo danh sách mới chứa các từ không có trong wordB
for word in wordA:
    if word not in wordB:
        result.append(word)

# Ghép lại thành chuỗi
a = " ".join(result)
print(f"Sau khi xóa, chuỗi a: \"{a}\"")
