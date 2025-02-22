class student:
    def __init__(self, id = "", avg = 0, age = 0, classes = ""):
        if len(id) != 8:
            raise ValueError("Lỗi: ID phải có đúng 8 ký tự!")

        if not (0 <= avg <= 10):
            raise ValueError("Lỗi: Điểm trung bình phải trong khoảng 0 - 10!")

        if age < 18:
            raise ValueError("Lỗi: Tuổi phải từ 18 trở lên!")

        if not (classes.startswith('A') or classes.startswith('C')):
            raise ValueError("Lỗi: Lớp phải bắt đầu bằng 'A' hoặc 'C'!")

        self.__id = id
        self.avg = avg
        self.age = age
        self.classes = classes

    def inputInfor(self):
        self.__id = input()
        self.avg = float(input())
        self.age = int(input())
        self.classes = input()

    def printInfor(self):
        print(f"ID: {self.__id}")
        print(f"Average: {self.avg}")
        print(f"Age: {self.age}")
        print(f"Classes: {self.classes}")
        print(f"Receive a scholarship: {self.checkReceiveAScholarship()}")

    def checkReceiveAScholarship(self):
        if self.avg >= 8:
            return "Yes"
        else:
            return "No"

    def __str__(self):
        return f"ID: {self.__id}\nName: {self.name}\nAge: {self.age}\nAverage: {self.avg}\nClasses: {self.classes}\nReceive a scholarship: {self.checkReceiveAScholarship()}"