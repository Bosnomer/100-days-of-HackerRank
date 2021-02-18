# Concatenate

import numpy as np
n,m,_=list(map(int,input().split()))
a=(np.array([input().split() for _ in range(n)],dtype=int))
b=(np.array([input().split() for _ in range(m)],dtype=int))
print(np.concatenate((a,b)))
