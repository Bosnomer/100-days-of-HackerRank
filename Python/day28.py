# itertools.combinations()

from itertools import combinations
from itertools import chain

a,b = input().split(" ")
b = int(b)
lst = []
lst[:0]=a
lst.sort()


tst=[]
for i in range(1,b+1):
    tst.append(list(combinations(lst,i)))
    #cleaned = [item for item in tst]
    cleaned = list(chain(*tst))

for i in cleaned:
    print("".join(i))
