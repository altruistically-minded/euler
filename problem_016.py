# -*- coding: utf-8 -*-
# Using Python 3
"""
   Power digit sum
   Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import time


tStart = time.time()
#####################################################
s  = 0
s  = 2 ** 1000

# list of digits
l = map(int, str(s))
print("sum of digits ")
print(l)
print(": %d", sum(l))

#####################################################
print("run time = " + str((time.time() - tStart)))
