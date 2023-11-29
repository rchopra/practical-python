# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    """Create a list representing the portfolio."""
    with open(filename) as lines:
        return parse_csv(lines, types=[str, int, float])


def read_prices(filename):
    """Read the prices file into a dictionary."""
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """Returns a list of the rows of the report."""
    rows = []
    for s in portfolio:
        name = s["name"]
        shares = s["shares"]
        curr_price = prices[name]
        change = curr_price - s["price"]
        rows.append((name, shares, curr_price, change))

    return rows


def print_report(report):
    """Print out the report data in a formatted table."""
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print("%10s %10s %10s %10s" % (("-" * 10,) * len(headers)))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {'$' + str(price):>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    """Read portfolio and price files and print out a formatted report."""
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
