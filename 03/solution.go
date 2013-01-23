package main

import (
  "fmt"
)

const (
  target int64 = 600851475143
)

var (
  _ = fmt.Println
)

func main() {
  filters := make(map[int]func(x int) bool)
  filters[2] = filter(2)
  for i := int64(3); i < target; i++ {
    if isprime(i, filters) {
      filters[i] := filter(i)
    }

  }
}

func isprint(int64 i, 

func filter(m int) func(x int) bool {
  return func(x int) bool {
    return x % m == 0
  }
}
