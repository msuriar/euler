#!/usr/bin/env python

digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

seconds = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    }

def main():
  count = 0
  for i in xrange(1,1001):
    count += countletters(num2string(i))
  print count

def countletters(s):
  return len(s.replace(' ',''))

def num2string(n):
  if n < 10:
    return digits[n]
  elif n < 20:
    return seconds[n]
  elif n < 100:
    t,u = n/10,n%10
    if u:
      return tens[n-u] + ' ' + num2string(u)
    else:
      return tens[n]
  elif n < 1000:
    h,r = n/100,n%100
    if r:
      return digits[h] + ' hundred and ' + num2string(r)
    else:
      return digits[h] + ' hundred'
  elif n == 1000:
    return 'one thousand'


if __name__ == "__main__":
  main()

