# No Idea!

n, m = map(int, input().split())

arr = input().split()

A = set(input().split())
B = set(input().split())
happiness = 0
happiness = sum([(i in A) - (i in B) for i in arr])

print(happiness)
