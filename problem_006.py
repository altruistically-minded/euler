"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

import time

def sumOfSquares(n):
    sum = 0
    for x in range(0,n+1):
        sum += x**2
    return sum

def squareOfSum(n):
    sum = 0
    for x in range(0,n+1):
        sum += x
    square = 0
    square = sum**2 
    return square

def sumOfSquares2(n):
    return n**2 * (n+1)**2 / 4

def squareOfSum2(n):
    return n * (n+1) * (2*n+1) / 6

def sumOfSquaresF(n):
    return n**2 * (n+1)**2 / 4

def squareOfSumF(n):
    return n * (n+1) * (2*n+1) / 6

n = 100

print "-"*20

tStart = time.time()
print "difference: ", squareOfSum(n) - sumOfSquares(n)
print "run time = " + str((time.time() - tStart))

print "-"*20
print "-"*20

tStart = time.time()
print "difference2: ", squareOfSum2(n) - sumOfSquares2(n)
print "run time = " + str((time.time() - tStart))

print "-"*20
