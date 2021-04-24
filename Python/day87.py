# Polynomials

import numpy as np
lst = list(map(float, input().split()))
print(np.polyval(lst, float(input())))
