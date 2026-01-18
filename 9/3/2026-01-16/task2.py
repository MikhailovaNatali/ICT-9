size = int(input())
a = [int(i) for i in range(0, size)]
for i in range(0, size):
    a[i] = int(input())
for j in range(1, size): 
    key = a[j]
    i = j
    while (i > 0 and a[i-1] > key):
        a[i] = a[i-1]
        i = i - 1
    a[i] = key
print(a)