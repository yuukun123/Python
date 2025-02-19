m = list(input().split())
k = []
is_zigzag = True

for i in range(len(m) - 1):
    if (m[i].isdigit() and m[i+1].isdigit()) or (m[i].isalpha() and m[i+1].isalpha()):
        is_zigzag = False
        break

if is_zigzag:
    for i in range(0, len(m) - 1, 2):
        if m[i].isdigit() and m[i+1].isalpha():
            k.append(int(m[i]) * len(m[i+1]))
        elif m[i].isalpha() and m[i+1].isdigit():
            k.append(len(m[i]) * int(m[i+1]))
else:
    print("None")

print(k)

# hello 1 hi
# 1 hii 3