# The Captain's Room

import collections

n = int(input())
arr = list(map(int, input().strip().split(' ')))

arr2 = ([item for item, count in collections.Counter(arr).items() if count > 1])
arr_set = set(arr)

for i in arr_set:
    if i not in arr2:
        print(i)
        break
