#!/usr/bin/env python

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def is_leap_year(n):
  if n % 4 != 0:
    return False
  elif n % 400 == 0:
    return True
  elif n % 100 == 0:
    return False
  else:
    return True

def get_length_of_month(date):
  y,m,d,_ = date
  if m == 2 and is_leap_year(y):
    return 29
  else:
    return months[m]

def add_month(date):
  y,m,d,day = date
  day1 = (day + get_length_of_month(date)) % 7
  if m < 12:
    return (y,m+1,d,day1)
  else:
    return (y+1,1,d,day1)

def main():
  for y in (1996, 2000, 1900, 1984, 1973):
    print "%d : %s" % (y, is_leap_year(y))

  print get_length_of_month((2002,1,2,0))

  date = (1900,12,1,6)

  count = 0
  while date[0] < 2001:
    date = add_month(date)
    if date[3] == 0:
      count += 1
  print count

if __name__ == "__main__":
  main()

