class stock:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol
        self.shares = shares
        self.price = price

    def get_symbol(self):
        return self.symbol
    def get_shares(self):
        return self.shares
    def get_price(self):
        return self.price

