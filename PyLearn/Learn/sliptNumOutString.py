n = "abd45ecf47wde3s1" * 1000000  # Chuỗi dài khoảng 8 triệu ký tự

# # các bình thường áp dụng hàm có sẵn
# num = 0
# for i in n:
#     if i.isdigit():
#         num += int(i)
# print(num)
#
# # tối ưu hơn
# n = "abd45ecf47wde3s1"
# num = sum(int(i) for i in n if i.isdigit())
# print(num)

# # giảm thời gian chạy xuống 1s
# import time
#
# start = time.time()
# num = sum(int(i) for i in n if '0' <= i <= '9')  # So sánh trực tiếp
# end = time.time()
# print("Thời gian:", end - start)

## dùng thử viện numpy
# import numpy as np
# import time
#
# start = time.time()
# numbers = [int(i) for i in n if '0' <= i <= '9']
# num = np.sum(numbers)
# end = time.time()
# print("tổng số: ", num, "Thời gian:", end - start)

# # xử lý song song
# from multiprocessing import Pool
# import time
#
# def sum_digits(chunk):
#     # Tính tổng các chữ số trong một đoạn
#     return sum(int(i) for i in chunk if '0' <= i <= '9')
#
# if __name__ == "__main__":
#     start = time.time()
#     num_chunks = 8  # Số lượng luồng (phụ thuộc vào số lõi CPU của bạn)
#
#     # Chia chuỗi thành các phần nhỏ
#     chunk_size = (len(n) + num_chunks - 1) // num_chunks  # Làm tròn lên
#     chunks = [n[i:i + chunk_size] for i in range(0, len(n), chunk_size)]
#
#     # Xử lý song song
#     with Pool(num_chunks) as pool:
#         results = pool.map(sum_digits, chunks)
#
#     total = sum(results)  # Tổng hợp kết quả
#     end = time.time()
#
#     print("Tổng:", total, "Thời gian:", end - start)

# dùng regex
import re
import time

start = time.time()
digits = re.findall(r'\d', n)  # Tìm tất cả chữ số
num = sum(map(int, digits))  # Chuyển thành số và tính tổng
end = time.time()

print("Tổng:", num, "Thời gian:", end - start)
