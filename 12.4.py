class Hexagon():
    def __init__(self, a):
        self.bok = a
        print("Utworzono sześcikąt")

    def calculate_perimeter(self):
        return self.bok * 6

hex1 = Hexagon(5)
print(hex1.calculate_perimeter())
    
