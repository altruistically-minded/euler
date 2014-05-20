# -*- coding: utf-8 -*-
# Using Python 3

import time
import math

from multiprocessing import Pool

"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

   n → n/2 (n is even)
   n → 3n + 1 (n is odd)

   Using the rule above and starting with 13, we generate the following sequence:

      13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
      It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

      Which starting number, under one million, produces the longest chain?

      NOTE: Once the chain starts the terms are allowed to go above one million.
"""


"""
input: starting number
output: length of Collatz sequence
"""
def collatz(n):
   length = 1

   while n != 1:
      if (n % 2) == 0:
         n = collatzEven(n)
      else:
         n = collatzOdd(n)

      length += 1

   return length

def collatzEven(n):
   return n/2

def collatzOdd(n):
   return 3*n+1

collatz(13)


tStart = time.time()
#####################################################
# Parallel Solution
pool = Pool()

args = range(1,1000000)
results = pool.map(collatz, args)

print("solution (parallel):")
print(results.index(max(results)) + 1)
#####################################################
print("run time = " + str((time.time() - tStart)))


print('\n'*2)

tStart = time.time()
#####################################################
# Serial solution

current_chain = 0
largest_chain = 0

starting_num_of_largest_chain = 0


for x in range(1,1000000):
   current_chain = collatz(x)

   if current_chain > largest_chain:
      largest_chain = current_chain
      starting_num_of_largest_chain = x


print("solution (serial):")
print(starting_num_of_largest_chain)

#####################################################
print("run time = " + str((time.time() - tStart)))



"""
http://stackoverflow.com/questions/20548628/how-to-do-parallel-programming-in-python

You can use the multiprocessing module. For this case I might use a processing pool:

   result1 = pool.apply_async(solve1, [A])    # evaluate "solve1(A)" asynchronously
   result2 = pool.apply_async(solve2, [B])    # evaluate "solve2(B)" asynchronously
   answer1 = result1.get(timeout=10)
   answer2 = result2.get(timeout=10)
   This will spawn processes that can do generic work for you. Since we did not pass processes, it will spawn one process for each CPU core on your machine. Each CPU core can execute one process simultaneously.

   If you want to map a list to a single function you would do this:

      args = [A, B]
      results = pool.map(solve1, args)
      Don't use threads because the GIL locks any operations on python objects.
"""


