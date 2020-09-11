#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here
  sorted_denominations = sorted(denominations, reverse=True)

  series = []

  for j in range(len(sorted_denominations)):
    t = sorted_denominations[j:]

    num_of_denominations = []
    total = amount
    for i in t:
      d = total // i
      total = total % i
      if d > 0:
        num_of_denominations.append((i, d))

    series.append(num_of_denominations)

  return series


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
