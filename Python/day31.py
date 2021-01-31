# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement
from itertools import chain

a,b = input().split(" ")
b = int(b)
lst = []
lst[:0]=a
lst.sort()


tst=[]
#for i in range(1,b+1):
tst.append(list(combinations_with_replacement(lst,b)))
cleaned = list(chain(*tst))

for i in cleaned:
    print("".join(i))
