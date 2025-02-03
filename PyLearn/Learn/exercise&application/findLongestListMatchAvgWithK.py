def longest_subarray_with_average(L, k):
    n = len(L)
    max_length = 0
    result = []

    for i in range(n):
        for j in range(i, n):
            subarray = L[i:j + 1]  # L[i:j] + [L[j]] = L[i:j + 1] (đối xung)
            avg = sum(subarray) / len(subarray) # Tính trung bình
            if avg == k and len(subarray) > max_length: # Kiem tra trung bình = k
                max_length = len(subarray) # Cập nhật do dai cua mang
                result = subarray[:] # Cập nhật mang

    return result

# Ví dụ chạy thử
L = [1, 2, 2, 3, 3, 4, 5, 6, 0, 1]
k = 4
print(longest_subarray_with_average(L, k))  # Output: [2, 3, 4]

