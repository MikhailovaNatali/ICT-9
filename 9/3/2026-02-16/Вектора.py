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
print("####")
for i in a:
    for j in a:
        if(angle(i, j) == 90):
            print(i)
            print(j)
print("####")
def projection(n, v):
    return  ((n@v)/(np.linalg.norm(v)))
print(projection(c, b))

#Ортогональный базис :
e1 = np.array([1, 0])
e2 = np.array([0, 1])

print("#####")
def Decomposition(r):
    x1 = (r@e1)/((np.linalg.norm(e1))**2)
    x2 = (r@e2)/((np.linalg.norm(e2))**2)
    print(x1)
    print(x2)
Decomposition(c)
