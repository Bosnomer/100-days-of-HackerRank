# Inner and Outer

import numpy as np

arr1 = np.array(input().split(), int)
arr2 = np.array(input().split(), int)
print(np.inner(arr1,arr2), np.outer(arr1,arr2), sep='\n')
