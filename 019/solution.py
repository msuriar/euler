#!/usr/bin/env python

months = (
    (1, 'January', 31),
    (2, 'February', 28),
    (3, 'March', 31),
    (4, 'April', 30),
    (5, 'May', 31),
    (6, 'June', 30),
    (7, 'July', 31),
    (8, 'August', 31),
    (9, 'September', 30),
    (10, 'October', 31),
    (11, 'November', 30),
    (12, 'December', 31)
)

def is_leap_year(n):
  if n % 4 != 0:
    return False
  elif n % 400 == 0:
    return True
  elif n % 100 == 0:
    return False
  else:
    return True

def main():
  for y in (1996, 2000, 1900, 1984, 1973):
    print "%d : %s" % (y, is_leap_year(y))

if __name__ == "__main__":
  main()

