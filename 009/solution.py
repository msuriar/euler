#!/usr/bin/env python

import math

def main():
  for x,y,z in find_pythagoreans(1000):
    if x + y + z == 1000:
      print x*y*z
      exit(0)

def find_pythagoreans(limit):
  for x in xrange(1, limit):
    for y in xrange(1, limit):
      z = math.sqrt(x**2 + y**2)
      if math.floor(z) == z:
        yield (x,y,int(z))

if __name__ == "__main__":
  main()
