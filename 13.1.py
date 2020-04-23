class Shape():
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b

    def what_am_i(self):
        print("Jestem figurą!")

class Rectangle(Shape):
    pass
        

    def calculate_perimeter(self):
        return 2 * (self.bok_a + self.bok_b)

class Square(Shape):
    def __init__(self, a):
        self.bok_a = a

    def calculate_perimeter(self):
        return 4 * self.bok_a

    def change_size(self, x):
        self.bok_a = self.bok_a + x
        if self.bok_a < 0:
            self.bok_a = 0
        

prostokat = Rectangle(5, 20)
print(prostokat.calculate_perimeter())

kwadrat = Square(5)
print(kwadrat.calculate_perimeter())

kwadrat.change_size(7)
print(kwadrat.calculate_perimeter())

kwadrat.change_size(-20)
print(kwadrat.calculate_perimeter())

prostokat.what_am_i()
kwadrat.what_am_i()



