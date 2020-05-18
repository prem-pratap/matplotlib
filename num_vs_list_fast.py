import numpy as np
import time
import sys
#first with 1000 then large size
size=1000000

#defining two lists
li1=range(size)
li2=range(size)

#defining two ndarrays
arr1=np.arange(size)
arr2=np.arange(size)

initial=time.time()

result1=[(x,y) for (x,y) in zip(li1,li2)]
print("Time taken to compute sume of list",time.time()-initial*1000)
initial=time.time()

result2=arr1+arr2

print("Time taken to compute sum of ndarray",time.time()-initial*1000)#multiplying by 1000 to convert sec into milliseconds

 
