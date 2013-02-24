#!/usr/bin/env python

smalldata = """
3
7 4
2 4 6
8 5 9 3""".strip()

bigdata = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".strip()

def parse_data(s):
  data = [ [ int(x) for x in r ] for r in [l.split() for l in s.splitlines()] ]
  return data

def get_children(node, data):
  r,c = node
  if r == len(data):
    return None
  else:
    child_row = r+1
    return ((child_row, c),(child_row,c+1))

def get_parents(node, data):
  r,c = node
  if r == 0:
    return None
  else:
    if c == 0:
      return ((r-1,c))
    elif c == len(data[r])-1:
      return ((r-1, c-1))
    else:
      return ((r-1, c-1),(r-1,c))

def main():
  d = parse_data(smalldata)
  print get_children((0,0), d)
  print get_parents((3,0), d)
  print get_parents((3,1), d)
  print get_parents((3,3), d)
  print d

if __name__ == "__main__":
  main()

