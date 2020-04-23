class Horse():
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

monia = Rider("Monika Żakiewicz")
kon_moni = Horse("Agat", "koń", monia)

print(kon_moni.rider.name)
