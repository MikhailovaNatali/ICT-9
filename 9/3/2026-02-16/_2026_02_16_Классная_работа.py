import numpy as np
import math
b = np.array([1, 0])
p = np.array([0, 1])
c = np.array([3, 4])
d = np.array([0, 4])
def angle(n, v):
    return  math.degrees(math.acos((n@v)/(np.linalg.norm(n)*np.linalg.norm(v))))
print(angle(b, p))
a = [b, p, c, d]
for i in a:
    for j in a:
        if(angle(i, j) == 90):
            print("###")
            print(i)
            print(j)
            
