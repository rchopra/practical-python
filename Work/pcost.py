# pcost.py
#
# Exercise 1.27

import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file."""
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit("Usage: %s portfoliofile" % args[0])
    filename = args[1]
    cost = portfolio_cost(filename)
    print(f"Total cost: {cost:0.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
