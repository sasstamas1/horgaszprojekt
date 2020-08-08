class Lake:
    def __init__(self, name, location, price, fish):
        self.name = name
        self.location = location
        self.price = price
        self.fish = fish

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getPrice(self):
        return self.price

    def getFish(self):
        return self.fish
