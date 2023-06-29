import numpy as np
a=np.array([1,2,3,4,5,6,7,8,0,5,8,0,4,0,6])
count=0
for i in a:
    if i==0:
        count+=1
print(count)