from student import student

if __name__ == '__main__':
    # std = student()
    # std.inputInfor()
    # std.printInfor()

    test_cases = [
        ("AB123456", 8.5, 20, "A1"),  # Hợp lệ
        ("AB12345", 7.0, 19, "C2"),  # ID sai
        ("CD789012", 10.5, 22, "A3"),  # Điểm TB sai
        ("EF567890", 7.5, 17, "C4"),  # Tuổi sai
        ("GH123456", 9.0, 21, "B5"),  # Lớp sai
        ("IJ654321", 8.0, 19, "A6"),  # Hợp lệ (học bổng)
        ("KL987654", 7.9, 20, "C7")  # Hợp lệ (không học bổng)
    ]

    for i, (__id, avg, age, classes) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        try:
            std = student(__id, avg, age, classes)
            std.printInfor()
        except ValueError as e:
            print(f"Lỗi: {e}")


