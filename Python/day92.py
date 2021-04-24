# Compress the String!

from itertools import groupby

for i, n in groupby(input()):
    lst= list(n)
    print("(", len(lst), ", ", lst[0], ")", end = " ", sep = "")
