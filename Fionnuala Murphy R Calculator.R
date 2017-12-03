add <- function(x, y) {
  return(x + y)
}

#test should return 6
add(4,2)


subtract <- function(x, y) {
  return(x - y)
}
#test should return 2
subtract(4,2)

multiply <- function(x, y) {
  return(x * y)
}
#test should return 8
multiply(4,2)

divide <- function(x, y) {
  return(x / y)
}
#test should return 2
divide(4,2)

square <- function(x) {
  return (x * x)
}
#test should return 16
square(4)

cube <- function(x) {
  return (x * x * x)
}
#test should return 64
cube(4)

exponential <- function (x,y) {
  return (x ^ y)
}
#test should return 16
exponential(4,2)

squareroot <- function(x) {
  return (sqrt(x))
}
#test should return 4
squareroot(16)

getcos <-function(x) {
  return (cos(x))
}
#test should return 0.814181
getcos(120)

gettan <- function(x) {
  return (tan(x))
}
#test should return 0.713123
gettan(120)

getsin <- function(x) {
  return (sin(x))
}
#test should return 0.5806112
getsin(120)

getfact <- function(x) {
  return(factorial(x))
}
#test should return 120
getfact(5)
