# Array Mathematics

import numpy as np
n,m = map(int,input().split())

a=np.zeros((n,m),int)
b=np.zeros((n,m),int)
for i in range(n):
  a[i]=np.array(input().split(),int)
for i in range(n):
  b[i]=np.array(input().split(),int)  

print(a+b)
print(a-b)
print(a*b)
print(np.array(a/b,int))
print(a%b)
print(a**b)
