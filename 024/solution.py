#!/usr/bin/env python

def permute(l):
  if len(l) < 2:
    output = [l]
  else:
    output = []
    for x in l:
      remnants = l[:]
      remnants.remove(x)
      for p in  permute(remnants):
        output.append([x] + p)
  return output

def main():
  foo = [''.join(s) for s in permute(list('0123456789'))]
  print foo[int(1E6)-1]

if __name__ == "__main__":
  main()

