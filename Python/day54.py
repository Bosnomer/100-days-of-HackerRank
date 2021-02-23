# Shape and Reshape

import numpy as np

arr = list(map(int, input().split()))[:9]
arr = np.array(arr)
print (np.reshape(arr,(3,3)))
