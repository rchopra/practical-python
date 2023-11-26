# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """Create a list representing the portfolio."""
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    """Read the prices file into a dictionary."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("WARNING: error reading", row)

    return prices


def make_report(portfolio, prices):
    rows = []
    for s in portfolio:
        name = s["name"]
        shares = s["shares"]
        curr_price = prices[name]
        change = curr_price - s["price"]
        rows.append((name, shares, curr_price, change))

    return rows


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
headers = ("Name", "Shares", "Price", "Change")
print("%10s %10s %10s %10s" % headers)
print("%10s %10s %10s %10s" % (("-" * 10,) * len(headers)))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {'$' + str(price):>10s} {change:>10.2f}")
