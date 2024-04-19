class Portfolio:
    def __init__(self):
        self.holdings = []

    def add(self, holding):
        self.holdings.append(holding)

    def total(self):
        return sum(self.holdings)
