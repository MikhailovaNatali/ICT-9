import string

a = input()
a = a.split(" ")
d = {}
for s in a:
    s = s.strip(string.punctuation).lower()

d = {a[i]: i + 1 for i in range(0, len(a))}
print(len(d))
