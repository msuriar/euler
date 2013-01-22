package main

import (
  "fmt"
)

func main() {
  total := 0
  f3 := multiples(3)
  f5 := multiples(5)
  f15 := multiples(15)
  for {
    if v:= f3(); v < 1000 {
      total += v
    } else {
      break
    }
  }
  for {
    if v:= f5(); v < 1000 {
      total += v
    } else {
      break
    }
  }
  for {
    if v:= f15(); v <1000 {
      total -= v
    } else {
      break
    }
  }

  fmt.Println(total)
}

func multiples(m int) func() int {
  count := 0
  return func() int {
    count++
    return m*count
  }
}
