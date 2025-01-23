m = list(input().split())

max_length = 0
index = 0

for i in range(len(m) - 1):
    if len(m[i]) > max_length:
        max_length = len(m[i])
        index = i

print(index)