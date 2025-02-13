# report.py
#
# Exercise 2.4


from . import fileparse, tableformat
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    """Read a stock portfolio file into a list of dictionaries with keys name, shares, and price."""
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )

    portfolio = [stock.Stock(**d) for d in portdicts]
    return Portfolio(portfolio)


def read_prices(filename):
    """Read the prices file into a dictionary."""
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    """Returns a list of the rows of the report."""
    rows = []
    for s in portfolio:
        curr_price = prices[s.name]
        change = curr_price - s.price
        rows.append((s.name, s.shares, curr_price, change))

    return rows


def print_report(reportdata, formatter):
    """Print out the report data in a formatted table."""
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    """Read portfolio and price files and print out a formatted report."""
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfile pricefile format" % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(
        filename="app.log",  # Name of the log file (omit to use stderr)
        filemode="w",  # File mode (use 'a' to append)
        level=logging.WARNING,  # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )

    main(sys.argv)
