# stock.py

from .typedproperty import Float, Integer, String


class Stock:
    """An instance of a stock holding consisting of name, shares, and price."""

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self):
        """Return the cost as shares*price."""
        return self.shares * self.price

    def sell(self, shares):
        """Sell a number of shares and return the remaining number."""
        self.shares -= shares
