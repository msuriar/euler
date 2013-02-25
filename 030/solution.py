#!/usr/bin/env python

import itertools

def main():
  total = 0
  for n in itertools.count(10):
    if n > len(str(n))*9**5:
      break
    if powers(n,5): total+=n
  print total

def powers(n, p):
  numbers = [int(c) for c in str(n)]
  return n == sum([x ** p for x in numbers])

if __name__ == "__main__":
  main()

