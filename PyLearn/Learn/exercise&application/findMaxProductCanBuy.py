def max_material(U, V, A, B):
    max_S = 0
    N = max(len(A), len(B))  # Số lượng công ty

    for i in range(N):
        for j in range(i + 1, N):
            # Lấy giá bán theo USD và EUR của công ty i
            A_i = A[i] if i < len(A) else float('inf')  # Nếu không có giá USD, coi là vô cùng lớn
            B_i = B[i] if i < len(B) else float('inf')  # Nếu không có giá EUR, coi là vô cùng lớn

            # Lấy giá bán theo USD và EUR của công ty j
            A_j = A[j] if j < len(A) else float('inf')  # Nếu không có giá USD, coi là vô cùng lớn
            B_j = B[j] if j < len(B) else float('inf')  # Nếu không có giá EUR, coi là vô cùng lớn

            # Case 1: i mua theo USD, j mua theo EUR
            S1 = (U / A_i) + (V / B_j) if A_i != 0 and B_j != 0 else 0
            # Case 2: i mua theo EUR, j mua theo USD
            S2 = (V / B_i) + (U / A_j) if B_i != 0 and A_j != 0 else 0
            # Case 3: cả hai mua theo USD
            S3 = (U / A_i) + (U / A_j) if A_i != 0 and A_j != 0 else 0
            # Case 4: cả hai mua theo EUR
            S4 = (V / B_i) + (V / B_j) if B_i != 0 and B_j != 0 else 0

            # Cập nhật max_S
            max_S = max(max_S, S1, S2, S3, S4)

    return round(max_S, 2)


# Ví dụ sử dụng
U = 100
V = 200
A = [10, 20, 30]  # Giá bán theo USD
B = [5, 15]  # Giá bán theo EUR (thiếu giá của công ty thứ 3)

result = max_material(U, V, A, B)
print(result)  # Output: 53.33