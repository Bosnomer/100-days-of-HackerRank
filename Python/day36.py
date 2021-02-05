# itertools.product()

from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l = (list(product(l1, l2)))
#print(type(l))
print(*l, sep=" ")
