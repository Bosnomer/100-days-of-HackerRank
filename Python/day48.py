# Set .difference() Operation

n = int(input())
arr1 = list(map(int, input().split()))[:n]
arr1=set(arr1)
m = int(input())
arr2 = list(map(int, input().split()))[:m]
arr2=set(arr2)
print(len(arr1.difference(arr2)))
