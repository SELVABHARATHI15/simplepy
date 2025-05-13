import numpy as np
arr = np.array([1,2,3,4,5])
print(type(arr)," ",arr)
# for i in arr:
#     print(i)
n = [True,True,False,True,False]
x = arr[n]
print(x)
print(np.__version__)