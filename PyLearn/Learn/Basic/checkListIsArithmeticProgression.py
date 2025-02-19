m = list(map(int, input().split()))
d = m[1] - m[0]

if len(m) < 2:
    print("not enough elements in the list")
else:
    is_arithmetic = True
    for i in range(1, len(m) - 1):
        if m[i + 1] - m[i] != d:
            is_arithmetic = False
            break

    if is_arithmetic:
        print("True")
    else:
        print("None")
