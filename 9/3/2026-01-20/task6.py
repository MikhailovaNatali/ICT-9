a = input()
a = a.split(" ")
d = {a[i]: i + 1 for i in range(0, len(a))}
print(d[a[len(a) -  1]])
