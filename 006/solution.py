#!/usr/bin/env python

def main():
  print sum_squares(10)
  print square_sum(10)
  print square_sum(100) - sum_squares(100)

def sum_squares(n):
  return sum( (x*x for x in xrange(n+1) ) )

def square_sum(n):
  return sum(xrange(n+1))**2

if __name__ == "__main__":
  main()
