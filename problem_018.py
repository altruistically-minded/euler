from copy import deepcopy

"""
###############################################################
                     Maximum path sum I
                        Problem 18
###############################################################
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

      3
     7 4
    2 4 6
   8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

   NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
      However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot 
      be solved by brute force, and requires a clever method! ;o)

"""

tri = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

tri = tri.split('\n')

# remove empty lines
tri = list(filter(None, tri))

rows = []
for line in tri:
    if line:
        cols = line.split(' ')
        c = []
        c = map(int, cols)
        rows.append(list(c))

max_path = []
currentIndex = 0

########################
# Print Triangle
########################
def printTriangle(rows):
   r = 0
   while r < len(rows):
      cols = rows[r]
      for c in cols:
         print(c, end=' ')
      print()
      r+=1
########################

printTriangle(rows)
print('\n'*3)

###################################
#     Top down iteration (wrong)
print("-"*30)
print("Top-down iteration (Greedy)")
print("-"*30)
###################################
print("start of loop")
r = 0
while r < len(rows):
   if r == 0:
      #print("rows[%d][%d] = %d" % (r, currentIndex, rows[r][currentIndex]))
      max_path.append(rows[r][currentIndex])
      r += 1
      continue
   #print("left: rows[%d][%d] = %d" % (r, currentIndex, rows[r][currentIndex]))
   #print("right: rows[%d][%d] = %d" % (r, currentIndex+1, rows[r][currentIndex+1]))
   left = rows[r][currentIndex]
   right = rows[r][currentIndex+1]
   if left > right:
      # choose left
      currentIndex = currentIndex
   else:
      # choose right
      currentIndex = currentIndex+1
   max_path.append(rows[r][currentIndex])
   r += 1
print("max_path:", end=' ')
print(max_path)
print("sum: %d" % sum(max_path))
###################################

print('\n'*3)

##########################################
#   Bottom up Greedy Solution (incorrect)
print("-"*30)
print("Bottom-up Greedy Solution")
print("-"*30)
##########################################
class Triangle:
   def __init__(self):
      self.Max = 0
      self.leftGreater = False
      self.ApexPos = 0

      self.Apex = 0
      self.lowerLeft = 0
      self.lowerRight = 0

   def setLeft(self, upper, lowerleft):
      self.Apex = upper
      self.lowerLeft = lowerleft
   
   def getLowerLeft(self):
      return self.lowerLeft

   def getLowerRight(self):
      return self.lowerRight

   def setRight(self, upper, lowerright):
      self.Apex = upper
      self.lowerRight = lowerright

   def getMax(self):
      self.leftHighest()
      return self.Max

   def leftHighest(self):
      l = self.Apex + self.lowerLeft
      r = self.Apex + self.lowerRight
      if l > r:
         self.Max = l
         self.leftGreater = True
      else:
         self.Max = r
         self.leftGreater = False
      return self.leftGreater
   
   def setApexPos(self, col):
      self.ApexPos = col

   def getApexPos(self):
      return self.ApexPos
      
   def getApex(self):
      return self.Apex

   def __repr__(self):
      s = ""
      s += "|Triangle: %s\n" % (self.Apex)
      s += "|\t %s %s\n" % (self.lowerLeft, self.lowerRight)
      s += "|Max: %s\n" % (self.Max)
      return s

   def __lt__(self, obj):
      if self.getMax() < obj.getMax():
         return -1


current = Triangle()
previous = Triangle()
maxPath = []


r = len(rows)-1
while r > 0:
   c = 0
   if r == len(rows)-1:
      while c < len(rows[r])-1:
         current.setLeft(rows[r-1][c], rows[r][c])
         current.setRight(rows[r-1][c], rows[r][c+1])
         current.setApexPos(c)

         if current > previous:
            previous = deepcopy(current)
         
         print("max: " + str(current.getMax()))
         c+=1
      print(previous)

      if previous.leftHighest():
         maxPath.append(previous.getLowerLeft())
      else:
         maxPath.append(previous.getLowerRight())

   # Now we work on chasing the Apex's up, until the Top 
   apexPos = previous.getApexPos()

   current = Triangle()
   previous = Triangle()

   if apexPos == 0:
      # We are looking at the left edge of the triangle
      previous.setLeft(rows[r-1][apexPos], rows[r][apexPos])
      previous.setApexPos(0)
      maxPath.append(previous.getApex())
      r-=1
      continue

   if apexPos == (len(rows[r])-1):
      # We are looking at the right edge of the triangle
      previous.setRight(rows[r-1][apexPos-1], rows[r][apexPos])
      previous.setApexPos(len(rows[r-1])-1)
      maxPath.append(previous.getApex())
      r-=1
      continue

   # Otherwise, we're in the middle of the triangle, and
   #  everything's gravy
   Left = Triangle()
   Right = Triangle()

   Left.setLeft(rows[r-1][apexPos-1], rows[r][apexPos])
   Left.setApexPos(apexPos-1)
   Right.setRight(rows[r-1][apexPos], rows[r][apexPos])
   Right.setApexPos(apexPos)

   previous = Triangle()
   if Left > Right:
      previous = deepcopy(Left)
   else:
      previous = deepcopy(Right)
   maxPath.append(previous.getApex())
   r-=1
print()
print(maxPath)
print("sum: %d" % sum(max_path))
##########################################

print('\n'*3)

##########################################
def SummationSolution(rows):
   r = len(rows)-2
   while r > -1:
      c = 0
      while c < len(rows[r]):
         rows[r][c] += max(rows[r+1][c], rows[r+1][c+1])
         c+=1
      r-=1
   print("sum: %d" % rows[0][0])

   print('\n'*3)
   printTriangle(rows)
##########################################
# Bottom-up summation solution
print("-"*30)
print("Bottom-up summmation solutions")
print("-"*30)
##########################################
SummationSolution(rows)
##########################################
