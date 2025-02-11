def encryptiionListToDic(n):
    if not n:
        return None

    m = {}  # Dictionary để lưu mã hóa
    encoded_list = []  # Danh sách đã mã hóa
    count = 0  # Biến đếm để gán số

    for word in n:
        if word not in m:
            m[word] = count
            count += 1
        encoded_list.append(m[word])  # Thêm giá trị m[word] vào danh sách

    return m, encoded_list

n = list(input().split())
m, encoded_list = encryptiionListToDic(n)

print(m)
print(encoded_list)