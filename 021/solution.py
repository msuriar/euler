#!/usr/bin/env python

def main():
  print score_file('names.txt')

def score_file(filename):
  l = get_data(filename)
  total = 0
  for i in xrange(len(l)):
    total += (i+1) * score_word(l[i])
  return total


def score_word(w):
  word = w.upper()
  total = 0
  for c in word:
    total += ord(c) - 64
  return total

def get_data(filename):
  f = open(filename)
  d = f.read()
  f.close()
  l = sorted([ x.strip('"') for x in d.split(',') ])
  return l

if __name__ == "__main__":
  main()

