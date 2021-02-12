# Set .symmetric_difference() Operation

n = int(input())
ar = list(map(int, input().strip().split(' ')))[:n]
ar = set(ar)
m = int(input())
br = list(map(int, input().strip().split(' ')))[:n]
br = set(br)

print(len(ar.symmetric_difference(br)))
