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
    square_list = []
    
    def __init__(self, a):
        self.bok_a = a
        self.square_list.append(a)
        print(""" Utworzono kwadrat o bokach {} na {} na {} na {}""".format(a, a, a, a))

    def calculate_perimeter(self):
        return 4 * self.bok_a

    def change_size(self, x):
        self.bok_a = self.bok_a + x
        if self.bok_a < 0:
            self.bok_a = 0

def check(a, b):
    if a is b:
        return True
    else:
        return False
    
        
kwadrat_1 = Square(5)
inny_kwadrat = kwadrat_1
kwadrat_2 = Square(6)
kwadrat_3 = Square(7)
kwadrat_4 = Square(8)

print(Square.square_list)
print(check(kwadrat_1, kwadrat_2))
print(check(kwadrat_1, inny_kwadrat))
