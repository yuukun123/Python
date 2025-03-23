from matrix import Matrix

if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])

    # m1 = Matrix.inputMaxtrix(2, 5)

    print(f"m1 \n{ m1 }", end= "\n\n")
    print(f"m2 \n{ m2 }", end= "\n\n")

    print(f"m1 + m2 \n{ m1 + m2 }", end= "\n\n")
    print(f"m1 - m2 \n{ m1 - m2 }", end= "\n\n")
    print(f"m1 * m2 \n{ m1 * m2 }", end= "\n\n")