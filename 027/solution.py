#!/usr/bin/env python

import itertools
import math

def gen_primes(n):
  D = {}
  for candidate in itertools.count(2):
    if candidate > n:
      break

    first_prime = D.pop(candidate, None)
    if first_prime is None:
      D[candidate*candidate] = candidate
      yield candidate
    else:
      next_multiple = candidate+first_prime
      while next_multiple in D:
        next_multiple+=first_prime
      D[next_multiple] = first_prime


def is_prime(n):
  if n < 2:
    return False

  limit = math.floor(math.sqrt(n))
  primes = gen_primes(limit)
  for prime in primes:
    if n % prime == 0:
      return False
  else:
    return True

def poly(a,b):
  def f(x):
    return x**2 + a*x + b
  return f

def conseq_primes(f):
  count = 0
  for x in itertools.count(0):
    if is_prime(f(x)):
      count += 1
    else:
      return count

def main():
  chain=a=b = 0
  for x in xrange(-1000, 1000):
    for y in xrange(-1000, 1000):
      nprimes = conseq_primes(poly(x,y))
      if nprimes > chain:
        chain,a,b = nprimes,x,y
  print chain,a*b

if __name__ == "__main__":
  main()

