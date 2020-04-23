import math

class Circle():
    def __init__(self, r):
        self.promien = r
        print("Utworzono okrąg")

    def area(self):
        return math.pi * (self.promien ** 2)

kolo = Circle(20)
print(kolo.area())
    
