#!/usr/bin/env python
lowerLimit = 0
upperLimit = 1000

total = sum(xrange(lowerLimit,upperLimit,3)) + sum(xrange(lowerLimit,upperLimit,5)) - sum(xrange(lowerLimit,upperLimit,15))
print total
