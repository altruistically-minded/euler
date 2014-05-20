# -*- coding: utf-8 -*-
# Using Python 3

"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


"""
   one
   two
   three
   four
   five
   six
   seven
   eight
   nine
   ten * 
   eleven
   twelve
   thirteen
   fourteen
   fithteen
   sixteen
   seventhteen
   eighteen
   nineteen
   twenty *
   twenty-one
   ...
   twenty-nine
   thirty * 
"""

import time

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

belowTwenty = ["ten", "eleven","twelve","thirteen","fourteen","fifteen",
               "sixteen","seventeen","eighteen","nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

f = open('log', 'w')

tStart = time.time()
#####################################################
length = 0
andFlag = False

for i in range(1,1001):
   s = ""
   andFlag = False

   # 1000
   if i == 1000:
      s += "one thousand"

      wordLength = len(s) - s.count(' ')
      length += wordLength
      f.write(s.ljust(30) + ":" + str(i).ljust(10) + "len: " + str(wordLength) + "\n")
      continue

   # divide by 100
   if i > 99:
      t = i / 100
      
      s += ones[int(t)-1]
      s += " hundred "
      andFlag = True

      lower = i % 100
   else:
      lower = i

   if lower != 0:
      remainder = 0

      if andFlag:
         s += "and "

      if lower < 20:
         if (lower < 10):
            remainder = lower
         else:
            # 10, 11, 12, ... 19
            s += belowTwenty[lower-10]
            s += " "
      else:
         tensDigit = lower / 10
         s += tens[int(tensDigit)-2]
         s += " "

         remainder = lower % 10

      # Ones digit
      if remainder != 0:
         s += ones[remainder-1]

   wordLength = len(s) - s.count(' ')
   length += wordLength
   f.write(s.ljust(30) + ":" + str(i).ljust(10) + "len: " + str(wordLength) + "\n")
print("Length: %d" % length)

#####################################################
print("run time = " + str((time.time() - tStart)))

