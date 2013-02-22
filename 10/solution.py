#!/usr/bin/env python

import itertools

def main():
  g = gen_primes()
  sum = 0
  for x in g:
    if 2E6 <= x:
      break
    else:
      sum += x
  print sum


def gen_primes():
  D = {}
  for q in itertools.count(2):
    p = D.pop(q, None)
    if p is None:
      yield q
      D[q*q] = q
    else:
      x = p + q
      while x in D:
        x += p
      D[x] = p

def is_prime(candidate, primes):
  for prime in primes:
    if candidate % prime == 0:
      return False
  else:
    return True

if __name__ == "__main__":
  main()

