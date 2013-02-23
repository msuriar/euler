package main

import (
  "fmt"
)

func main() {
  f := fib()

  total := 0
  for i := f(); i <= 4E6; i = f() {
    if i % 2 == 0 {
      total += i
    }
  }

  fmt.Println(total)
}

func fib() func() int {
  x,y := 1,1
  return func() int {
    x,y = y,x+y
    return x
  }
}
