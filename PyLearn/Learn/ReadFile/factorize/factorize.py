from math import sqrt

def factorize():
    try:
        with open("thuaso.inp", "r") as fr, open("thuaso.out", "w") as fw:
            for num in map(str.strip,fr):
                if not num:
                    continue

                num = int(num)
                ls = []

                # xử lý các số 2 trước để vào loop chỉ duyệt số lẻ
                while num % 2 == 0:
                    ls.append("2")
                    num //= 2

                for i in range(3, int(sqrt(num)) + 1, 2):
                    while num % i == 0:
                        ls.append(str(i))
                        num //= i
                # nếu còn lại snt > 1 thì thêm vào kết quả
                if num > 1:
                    ls.append(str(num))
                fw.write(" ".join(ls) + "\n")

    except FileNotFoundError:
        print("File not found")

factorize()