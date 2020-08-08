class Fishing:
    def __init__(self, date, Lake, Fishs, withwho):
        self.date = date
        self.Lake = Lake
        self.Fishs = Fishs
        self.withwho = withwho

    def getDate(self):
        return self.date

    def getLake(self):
        return self.Lake

    def getFishs(self):
        return self.Fishs

    def getWithwho(self):
        return self.withwho
