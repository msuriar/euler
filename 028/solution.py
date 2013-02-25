#!/usr/bin/env python

def make_grid(n):
  if n % 2 == 0:
    return None

  output = [ [None]*n for _ in range(n) ]
  return output

def get_next_coords(r,c,d,g):
  if d == 'left':
    y,x = r,c-1
    if x < 0 or g[y][x] != None:
      return get_next_coords(r,c,'down',g)
    else:
      return (y,x,'left')
  elif d == 'down':
    y,x = r+1,c
    if y >= len(g) or g[y][x] != None:
      return get_next_coords(r,c,'right',g)
    else:
      return (y,x,'down')
  elif d == 'right':
    y,x = r,c+1
    if x >= len(g) or g[y][x] != None:
      return get_next_coords(r,c,'up',g)
    else:
      return (y,x,'right')
  elif d == 'up':
    y,x = r-1,c
    if y < 0 or g[y][x] != None:
      return get_next_coords(r,c,'left',g)
    else:
      return (y,x,'up')


def spiral(grid):
  n = len(grid)
  count = n**2
  r,c = 0, n-1
  d = 'left'
  while count > 0:
    grid[r][c] = count
    count -= 1
    if count == 0:
      break
    else:
      r,c,d = get_next_coords(r,c,d,grid)
  return grid

def sum_diagonals(g):
  return sum_diag(g,False) + sum_diag(g,True) - 1

def sum_diag(g,invert):
  n = len(g)
  total = 0
  for x in range(n):
    if invert:
      total += g[n-x-1][x]
    else:
      total += g[x][x]
  return total


def main():
  g = spiral(make_grid(1001))
  print sum_diagonals(g)


if __name__ == "__main__":
  main()
