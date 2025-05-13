import numpy as np
arrc = np.array([12,23,34,45,56])
fil = []
for i in arrc:
    if i%2==0:
        fil.append(True)
    else:
        fil.append(False)
x = arrc[fil]
print(x)
print(np.__version__)