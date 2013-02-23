#!/usr/bin/env python

def main():
  top = (0,0)
  for i in xrange(1,int(1E6)):
    cl = collatz_length(i)
    if cl > top[1]:
      top = (i, cl)
  print top

def collatz_length(n):
  count = 0
  term = n
  while term != None:
    term,count = collatz(term),count+1
  return count

def collatz(n):
  if n == 1:
    return None
  elif n % 2 == 0:
    return n/2
  else: # n % 2 == 1
    return 3*n+1

if __name__ == "__main__":
  main()

