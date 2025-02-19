from datetime import datetime, timedelta, date, MAXYEAR, MINYEAR
import time

# newDate = datetime(2023, 1, 1)
# # newDate = newDate + datetime.timedelta(days=1)
# print(newDate)

# Tạo một đối tượng timedelta biểu diễn khoảng thời gian 5 ngày
delta = timedelta(days=2, hours=3, minutes=30, seconds=15)

# Lấy ngày hiện tại
now = date(MINYEAR, 1, 1)

# Lấy ngày hiện tại theo kieu timestamp
now = date.fromtimestamp(time.time())

# Tính toán ngày trong tương lai
future_date = now + delta
print(f"Ngày hiện tại: {now}")
print(f"Ngày trong tương lai (sau 5 ngày): {future_date}")
