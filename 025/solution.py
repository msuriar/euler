#!/usr/bin/env python
import math

def fib():
  x,y = 1,1
  yield x
  while True:
    x,y = y,x+y
    yield x

def main():
  f = fib()
  i = 0
  for n in f:
    i += 1
    if len(str(n)) >= 1000:
      print "F%d : %d" % (i, n)
      exit(0)

if __name__ == "__main__":
  main()

