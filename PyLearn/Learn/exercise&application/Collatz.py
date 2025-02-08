def Collatz(n):
    for i in range(1, n + 1):
        ls = []
        tmp = i
        while tmp != 1:
            ls.append(tmp)
            # tmp & 1 == 0
            if tmp & 1: # sử dụng bit & 1 để ktra xem tmp co phai la so le hay khong
                tmp = 3 * tmp + 1
            else:
                # sử dụng chia bit trên 2
                tmp = tmp >> 1 # tmp = tmp // 2
        ls.append(1)
        print(','.join(map(str, ls)), end = ' ')
    pass


n = int(input())
# Collatz(n)
# n = n >> 2
n = n & 104
print(n)


