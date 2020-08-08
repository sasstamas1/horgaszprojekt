class Fish:
    def __init__(self, name, size, date, time, bait):
        self.name = name
        self.size = size
        self.date = date
        self.time = time
        self.bait = bait

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getTime(self):
        return self.time

    def getBait(self):
        return self.bait
