# itertools.permutations()

from itertools import permutations

ip,n = input().split()

ip = list(ip)
n = int(n)
lst = list(permutations(ip,n))

lst1 = []
for i in lst:
    j = ''.join(i)
    lst1.append(j)

lst1.sort()
for i in lst1:
    print(i)
