#!/usr/bin/env python

import re

def get_repeat(n):
  data = []
  repeat = False
  remainder = 1
  for _ in xrange(n):
    remainder = remainder % n
    if remainder == 0:
      break
    elif remainder in data:
      repeat = True
      break
    else:
      data.append(remainder)
      remainder *= 10
  return (repeat,data)

def main():
  number,repeat = 1,1
  for i in xrange(1000):
    r,d = get_repeat(i)
    if r and len(d) > repeat:
      number,repeat = i,len(d)
  print number,repeat

if __name__ == "__main__":
  main()

