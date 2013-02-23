#!/usr/bin/env python

import itertools
import math
import operator

def gen_primes():
  D = {}
  for c in itertools.count(2):
    factor = D.pop(c, None)
    if factor == None:
      # c is prime
      yield c
      # c*c is not prime, has a factor of itself
      D[c*c] = c
    else:
      # c is not prime and is a multiple of factor
      # Find the next multiple of factor which we don't know about
      # Insert that multiple into dict, with a factor of factor
      x = c + factor
      while x in D:
        x += factor
      D[x] = factor

def triangles():
  output = 0
  for x in itertools.count(1):
    output += x
    yield output

def num_factors(n):
  if n == 1:
    return 1

  counts = almost_prime_factors(n)
  counts.pop(1)
  for k in counts:
    counts[k] += 1
  return reduce(operator.mul, counts.values())

def almost_prime_factors(n):
  g = gen_primes()
  remainder = n
  counts = {}
  counts[1] = 1
  while remainder > 1:
    for p in g:
      if remainder < 2:
        break
      else:
        while remainder % p == 0:
          counts[p] = counts.get(p, 0) + 1
          remainder = remainder / p
  return counts


def main():
  foo = triangles()
  for num in foo:
    if num_factors(num) > 500:
      print num
      exit(0)

if __name__ == "__main__":
  main()

