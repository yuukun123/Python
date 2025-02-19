from datetime import date

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate

    def calculate_age(self): # tính tuổi
        today = date.today() # ngày hien tai
        age = today.year - self.birthdate.year # tính tuổi
        # Neu ngày hien tai chua toi ngày sinh
        # thi giam tuoi di 1
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Age: {self.calculate_age()}")


person1 = Person("John Doe", "USA", date(1990, 3, 1))
person1.show_info()
