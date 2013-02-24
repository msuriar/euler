#!/usr/bin/env python

def main():
  total = 0
  for i in xrange(10000):
    if is_amicable(i):
      total += i
  print total

def is_amicable(n):
  return d(d(n)) == n and d(n) != n

def d(n):
  return sum(divisors(n))

def divisors(n):
  results = []
  limit = n/2
  for d in xrange(limit, 0, -1):
    if n % d == 0:
      results.append(d)

  return results

if __name__ == "__main__":
  main()

