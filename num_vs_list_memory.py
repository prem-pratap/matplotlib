import numpy as np
import time
import sys


li=range(1000)
#memory occupied by arr and  list in bytes
print(sys.getsizeof(2))
print(sys.getsizeof(5)*len(li))

arr=np.arange(1000)
print(arr.size*arr.itemsize)
