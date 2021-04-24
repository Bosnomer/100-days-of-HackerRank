# Find Angle MBC

import math
lAB, lBC = int(input()),int(input())

lAC = math.hypot(lAB, lBC)       
res = round(math.degrees(math.acos(lBC/lAC)))  
degree=chr(176)                                
print(res,degree, sep='')
