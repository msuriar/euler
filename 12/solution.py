#!/usr/bin/env python

import itertools
import math

def triangles():
  output = 0
  for x in itertools.count(1):
    output += x
    yield output

def num_factors(n):
  count = 1
  top = int(math.floor(n/2))
  for x in xrange(top, 0, -1):
    if n % x == 0:
      count += 1
  return count

def main():
  foo = triangles()
  for i in foo:
    if num_factors(i) > 500:
      print i
      exit(0)

if __name__ == "__main__":
  main()

