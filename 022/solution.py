#!/usr/bin/env python

def divisors(n):
  limit = n/2
  output = []
  for i in xrange(1,limit+1):
    if n % i == 0:
      output.append(i)
  return output

def abundant(n):
  return sum(divisors(n)) > n

def perfect(n):
  return sum(divisors(n)) == n

def deficient(n):
  return sum(divisors(n)) < n

def abundants(limit):
  output =[]
  for i in xrange(12,limit+1):
    if abundant(i):
      output.append(i)
  return output

def abundant_pairs(limit,v=False):
  a = abundants(limit)
  c = [False]*(limit+1)
  if v:
    print "a: " , a
    print "len(a): %d" % len(a)
    print "C: " , c
    print "len(c): %d" % len(c)
  for i in xrange(len(a)):
    current = a[i]
    if v: print "Current: %d" % current
    if 2*current < len(c):
      if v: print "Setting c[%d] : True\n" % (2*current)
      c[2*current] = True

    for j in xrange(i+1,len(a)):
      pair = a[j]
      if current+pair >= len(c):
        break
      else:
        c[current+pair] = True
  return c

def main():
  c = abundant_pairs(21823)
  # a = abundants(100)
  # print a
  total = 0
  for i in xrange(len(c)):
    if not c[i]:
      total += i
  print total

if __name__ == "__main__":
  main()

