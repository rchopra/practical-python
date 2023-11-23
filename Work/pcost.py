# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    """Calculate protfolio cost."""
    total = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", row)

    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost {cost:0.2f}")
