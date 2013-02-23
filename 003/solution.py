#!/usr/bin/env python

def main():
  print largest_prime_factor(600851475143)


def largest_prime_factor(n):
  divisor = 2
  total = n
  while total > 1:
    while total % divisor == 0:
      total = total / divisor
    divisor += 1
  return divisor-1

if __name__ == "__main__":
  main()
