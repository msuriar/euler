#!/usr/bin/env python

upperLimit = 4000000

fibIndexUpperLimit = 34


def fib(n, current = 0, next = 1):
  if n == 0:
    return current
  else:
    return fib(n-1, next, current+next)

print sum([fib(x) for x in xrange(34) if fib(x)%2 == 0 ])
