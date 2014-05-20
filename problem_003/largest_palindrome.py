"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/thread=4
"""


# Let's iterate through each possible 2-digit number, starting from 99 and decrementing, and see if we also get 9009

def isPalindrome(a):
    n = str(a)

    """
    We're checking if the string representation of n equals the inverted string representation of n
    The [::-1] slice takes care of inverting the string
    After that, we compare for equality using ==
    """
    #[::-1] is advanced slicing. [a:b:c] means slice from a (inclusive) to b (exclusive) with step size c
    return str(n) == str(n)[::-1]

import time


def largest_two_digit_palindrome():
    x = 999
    y = 999
    sol = 0

    found = False
    yTurn = True

    while not found:
        if isPalindrome(x*y):
                 if (x*y) > sol:
                     sol = x*y
        if yTurn:
            yTurn = not yTurn
            y -= 2
        else:
            yTurn = not yTurn
            x -= 1
        if x < 0:
            break
        if y < 0:
            break
    print "x: ", x
    print "y: ", y
    return sol

def brute_force():
    x = 999
    y = 999
    sol = 0

    for x in range(0,999):
        for y in range(0,999):
            if isPalindrome(x*y):
                if (x*y) > sol:
                    sol = x*y

    return sol


tStart = time.time()
print "largest two digit palindrome(): ", largest_two_digit_palindrome() 
print "run time = " + str((time.time() - tStart))

tStart = time.time()
print "brute_force", brute_force() 
print "run time = " + str((time.time() - tStart))

