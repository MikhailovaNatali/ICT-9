import matplotlib.pyplot as plt
import numpy as np

n = 4
X = np.array([-9, -4, -1, 7])
Y = np.array([5, 2, -2, 9])

def l(x, i):
    answer = 1
    for j in range(0, n):
        if(i != j):
            answer = answer*((x - X[j])/(X[i] - X[j]))
    return answer
def L(x):
    answer = 0
    for i in range(0, n):
        answer = answer + Y[i]*l(x, i)
    return answer

X1 = np.linspace(-20, 20, 1000)
Z = L(X1)
plt.plot(X1, Z, color = "m")
plt.show()