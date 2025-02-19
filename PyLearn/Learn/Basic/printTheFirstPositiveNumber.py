m = list(map(int, input().split()))
found = False

for i in m:
    if i > 0:
        print(i)
        found = True
        break

if not found:
    print(-1)