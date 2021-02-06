# collections.Counter()

from collections import Counter

x = int(input())
l = list(map(int,input().strip().split()))[:x]
n = int(input())

total = 0

keys = list(Counter(l).keys())
values = list(Counter(l).values())

for i in range(n):
    cust = list(map(int,input().strip().split()))[:2]
    if(cust[0] in keys):
        idx = keys.index(cust[0])
        values[idx] = values[idx]-1
        if (values[idx]>=0):
            total=total+cust[1]
        else:
            continue
        
print(total)
