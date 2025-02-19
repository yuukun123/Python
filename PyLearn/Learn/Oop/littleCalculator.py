class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        self.x = x
        self.y = y
        return self.x + self.y
    def sub(self):
        self.x = x
        self.y = y
        return self.x - self.y
    def mul(self):
        self.x = x
        self.y = y
        return self.x * self.y
    def div(self):
        if y != 0:
            return self.x / self.y
        else:
            return "khong chia duoc"

    def showCalculate(self):
        print(f"{self.x} + {self.y} = {self.add()}")
        print(f"{self.x} - {self.y} = {self.sub()}")
        print(f"{self.x} * {self.y} = {self.mul()}")
        print(f"{self.x} / {self.y} = {self.div()}")

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
cal = calculator(x,y)
cal.showCalculate()