def MaxIndex(a):
    maxIndex = 0
    for i in range(1, len(a)):
        if a[i] > a[maxIndex]:
            maxIndex = i
    return maxIndex

m = list(map(int, input().split()))
print(MaxIndex(m))