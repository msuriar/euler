#!/usr/bin/env python


def main():
  print find_smallest_multiple(20)

def find_smallest_multiple(limit):
  candidate = limit*2
  while True:
    if check_num(candidate, limit):
      return candidate
    else:
      candidate += limit



def check_num(candidate, limit):
  for num in xrange(1,limit+1):
    if candidate % num != 0:
      return False
  else:
    return True

if __name__ == "__main__":
  main()
