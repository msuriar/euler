#!/usr/bin/env python

def distinct_powers(a,al,b,bl):
  data = set()
  for base in xrange(a,al+1):
    for power in xrange(b,bl+1):
      data.add(base ** power)
  return data

def main():
  print len(distinct_powers(2,100,2,100))

if __name__ == "__main__":
  main()

