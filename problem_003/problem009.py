# -*- coding: utf-8 -*-

"""
=================================================================
                    Sieve of Eratosthenes
=================================================================
Input: an integer n > 1
 
Let A be an array of Boolean values, indexed by integers 2 to n,
initially all set to true.

for i = 2, 3, 4, ..., not exceeding sqrt(n):
    if A[i] is true:
        for j = i2, i2+i, i2+2i, ..., not exceeding n :
            A[j] := false

Output: all i such that A[i] is true.

"""
import time
from math import sqrt

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

def farey( n, asc=True ):
    seq = [] 

    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1  , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1 , n     # (*)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        p = Point()
        p.x = a
        p.y = b
        seq.append(p)
    return seq
        

def genTFtable(n):
    l = [True]*(n+1)

    for i in range(2, n+1):
        if l[i]:
            for x in range(i*2,n+1,i):
                l[x] = False
    return l

def genPrimes(n):
    truthTable = genTFtable(n)

    primes = []

    for x in range(0, len(truthTable)):
        if truthTable[x]:
            primes.append(x)
    return primes

#n = 20

tStart = time.time()
###########################################################################
n = 1000
f = farey(n)
possible = []

for i in f:
    a = i.x
    b = float(i.y)

    print "%d, %d" % (a, b)
    # Possible match
    c = 0
    c = sqrt(a**2 + b**2)
    if (a + b + c) == 1000:
        possible.append((a,b,c))
print '-'*20
print possible 

###########################################################################
print "run time = " + str((time.time() - tStart))

def brute_force(n):
    possible = []
    for a in range(0,n):
        for b in range(0,n):
            c = sqrt(a**2 + b**2)
            if (a+b+c) == 1000:
                possible.append((a,b,c))
    return possible

tStart = time.time()
###########################################################################
n = 1000
possible = brute_force(n)
print possible

###########################################################################
print "run time = " + str((time.time() - tStart))


