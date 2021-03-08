# Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

x, y = map(int, input().split())

print(numpy.eye(x, y))
