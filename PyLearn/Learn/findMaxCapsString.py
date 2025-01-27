m = list(input("Nhập danh sách các chuỗi: ").split())

max_index = -1  # Lưu vị trí ký tự in hoa lớn nhất
result = ""  # Lưu chuỗi có vị trí ký tự in hoa lớn nhất

for s in m:
    # Duyệt qua chuỗi để tìm vị trí ký tự in hoa lớn nhất
    for i in range(len(s)):
        if s[i].isupper():
            if i > max_index:  # So sánh với vị trí lớn nhất hiện tại
                max_index = i
                result = s  # Cập nhật chuỗi kết quả

if result == "":
    print("Không có ký tự in hoa trong danh sách.")
else:
    print("Chuỗi có vị trí ký tự in hoa lớn nhất:", result)


