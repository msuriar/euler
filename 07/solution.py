#!/usr/bin/env python


def main():
  print gen_primes(10001)[-1]

def gen_primes(count):
  primes = [2]
  candidate = 3
  while len(primes) < count:
    if is_prime(candidate, primes):
      primes.append(candidate)
    candidate += 2
  return primes

def is_prime(candidate, primes):
  for prime in primes:
    if candidate % prime == 0:
      return False
  else:
    return True



if __name__ == "__main__":
  main()
