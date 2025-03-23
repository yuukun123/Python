class product:
    def __init__(self, name = "", description = "", price = 0):
        self.name = name
        self.description = description
        if 0 < price <= 100:
            self.price = price
        self.Rates = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description

    def getDescription(self):
        return self.description

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def addRate(self, rate):
        if 1 <= rate <= 5:
            self.Rates.append(rate)
        else:
            print(f"your rate {rate} invailid, please input rate from 1 to 5")

    def get_avg_rate(self):
        if not self.Rates:
            return 0
        return sum(self.Rates) / len(self.Rates)

    def viewInfo(self):
        avg_rate = self.get_avg_rate()
        return f"Tên: {self.name}\nMô tả: {self.description}\nGiá: {self.price}\nĐánh giá trung bình: {avg_rate:.1f} (Tổng {len(self.Rates)} đánh giá)"