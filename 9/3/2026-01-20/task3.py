size = int(input())
a = [None for _ in range(size)]
for i in range(0, size): 
    a[i] = input()
    a[i] = a[i].capitalize()
print(a)


