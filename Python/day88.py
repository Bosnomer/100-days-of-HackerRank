# Linear Algebra

import numpy as np

print(round(np.linalg.det(np.array([list(map(float,input().split())) 
    for _ in range(int(input()))])),2))
