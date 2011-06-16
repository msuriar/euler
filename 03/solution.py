#!/usr/bin/env python
def getPrimes(n):
  numbers = set(range(2, n))
  limit = max(numbers)
  n = 2
  while (n != max(numbers)):
    numbers = removeMultiples(n, numbers)
    foo = numbers.copy()
    foo.discard(n)
    print foo
    n = min(foo)
  return numbers

def removeMultiples(base, collection):
  limit = max(collection)
  multiplier = 2
  while (multiplier * base < limit):
    collection.discard(multiplier * base)
    multiplier += 1
  return collection

def factorise(x):
  n = 2
  factors = []
  while (x != 1):
    while (x%n == 0):
      factors.append(n)
      x = x / n
    n = n+1
  return factors
