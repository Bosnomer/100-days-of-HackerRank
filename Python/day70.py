# Mean, Var, and Std

import numpy

nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for i in range(n):
    m = list(map(int, input().split()))
    arr.append(m)
arr = numpy.array(arr)

mean = numpy.mean(arr, axis = 1)
var = numpy.var(arr, axis = 0)
std = numpy.std(arr)

print(mean)
print(var)

rnd = numpy.around(std, 11)
print(rnd)
