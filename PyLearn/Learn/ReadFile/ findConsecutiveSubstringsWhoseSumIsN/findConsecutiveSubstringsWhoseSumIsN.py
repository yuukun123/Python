def findSubArrays(n):
    result = []
    count = 0
    # Duyệt qua các số bắt đầu từ 1
    for start in range(1, n):
        total = start
        next_num = start + 1

        # Tính tổng dãy số liên tiếp
        while total < n:
            total += next_num
            next_num += 1

            if total == n:
                count += 1
                result.append("+".join(map(str, range(start, next_num))))
                break

    return count, result

def findConsecutiveSubstringsWhoseSumIsN():
    try:
        with open('bieudienso.inp', 'r') as fr, open('bieudienso.out', 'w') as fw:
            n = int(fr.read().strip())
            cnt, subArray = findSubArrays(n)
            if cnt == 0:
                print("0")
                fw.write("0\n")
            else:
                print(cnt)
                fw.write(str(cnt) + "\n")

                print("\n".join(subArray))
                fw.write("\n".join(subArray) + "\n")

    except Exception as e:
        print(e)

findConsecutiveSubstringsWhoseSumIsN()


