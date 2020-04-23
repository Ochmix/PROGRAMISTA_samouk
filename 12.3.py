class Triangle():
    def __init__(self, a, h):
        self.podstawa = a
        self.wysokosc = h
        print("Stworzona trójkąt!")

    def area(self):
        return (self.podstawa * self.wysokosc) / 2

trojkat_1 = Triangle(4, 6)
print(trojkat_1.area())
    
