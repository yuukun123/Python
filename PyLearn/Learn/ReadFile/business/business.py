def calculateMoney(x):
    return (x[1] - x[0])

def calculateBusiness():
    try:
        with open("kinhdoanh.inp", "r") as fr, open("kinhdoanh.out", "w") as fw:
            n = int(fr.readline().strip())
            total_profit = 0

            for _ in range(n):
                M, B = map(int, fr.readline().strip().split())
                total_profit += calculateMoney((M, B))

            print(total_profit)
            fw.write(str(total_profit) + "\n")

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid input")

calculateBusiness()