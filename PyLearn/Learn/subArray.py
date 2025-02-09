def subArray(L):
    n = len(L)
    result = []
    for i in range(n):
        for j in range(i, n):
            subarray = L[i:j + 1]  # L[i:j] + [L[j]] = L[i:j + 1] (đối xung)
            result.append(subarray)
            print(subarray)
        print()

    # for i in range (n):
    #     subarray = L[i:i + 1]
    #     print(subarray)

L = [1, 2, 3, 4, 5]
subArray(L)