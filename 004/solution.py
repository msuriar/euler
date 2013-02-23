#!/usr/bin/env python

def main():
  print max(find_palindromic_numbers())

def find_palindromic_numbers():
  first,second = xrange(999,100,-1), xrange(999,100,-1)
  palindromes = []
  for i in first:
    for j in second:
      product = i * j
      if palindrome(product):
        palindromes.append(product)
  return palindromes

def palindrome(n):
  s = str(n)
  if len(s) % 2 == 0:
    midpoint = len(s)/2
    first_half = s[:midpoint]
    second_half = reversed(s[midpoint:])
  else:
    # Odd number of elements
    midpoint = len(s)/2
    first_half = s[:midpoint]
    second_half = reversed(s[midpoint+1:])

  for k,v in zip(first_half,second_half):
    if k != v:
      return False
  else:
    return True



if __name__ == "__main__":
  main()
