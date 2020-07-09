#!usr/bin/env python3
import matplotlib.pyplot as plt
import mpld3
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="First Group")
plt.bar([3,4,6,8,10],[8,6,2,5,6],label="Second Group")
plt.legend()
#giving labels to axis
plt.ylabel("Height")
plt.xlabel("Number")
plt.title("Bar Graph")
#plt.show()
mpld3.show()
