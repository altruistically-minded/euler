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

n = 1000000
#n = 20

tStart = time.time()
primes = genPrimes(n)
print "run time = " + str((time.time() - tStart))

#print primes
print primes[6+1]

print "primes found:", len(primes)
if len(primes) > 10001:
    print primes[10001+1]





