class Number:
    def __init__(self, listt):
        self.list = listt

    def avarage(self):
        return sum(self.list) / len(self.list)
