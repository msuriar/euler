#!/usr/bin/env python

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

def make_score_tree(data):
  scores = []
  for row in data:
    scores.append([0]*len(row))
  return scores

def find_max_values(l,t):
  v = 0
  for r,c in l:
    v = max(v,t[r][c])
  return v


def score(d):
  s = make_score_tree(d)
  s[-1] = d[-1][:]
  for r in xrange(len(d)-2,-1, -1):
    for i in xrange(len(s[r])):
      s[r][i] = d[r][i] + find_max_values(get_children((r,i), s), s)
  return s

def main():
  f = open('triangle.txt', 'r')
  data = f.read().strip()
  f.close()
  d = parse_data(data)

  s = score(d)
  print s[0][0]

if __name__ == "__main__":
  main()

