def precompute_sequence(limit=1000):
    """Tính trước dãy số lên tới a[limit]"""
    num = [1, 1, 1] + [0] * (limit - 3)
    for i in range(3, limit):
        num[i] = num[i - 1] + num[i - 3]
    return num

def stringNums():
    num = precompute_sequence(1000)
    with open("dayso.inp", "r") as fr, open("dayso.out", "w") as fw:
        for a in map(str.strip, fr):
            a = int(a)
            print(num[a - 1], end=' ')
            fw.write("".join(str(num[a - 1])) + "\n")

stringNums()
