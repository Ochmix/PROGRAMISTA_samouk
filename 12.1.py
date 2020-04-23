class Apple():
    def __init__(self, w, c, t, s):
        self.weight = w
        self.color = c
        self.taste = t
        self.species = s
        print("Utworzono Jabłko")


ap1 = Apple(135, "czerwone", "słodkie", "yonagold")
print(ap1)
print(ap1.weight)
print(ap1.color)
print(ap1.taste)
print(ap1.species)
