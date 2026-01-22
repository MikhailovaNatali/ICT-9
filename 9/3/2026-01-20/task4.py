a = input()
b = "aeuio"
c = "qwrtypsdfghjklzxcvbnm"
e = 0
d = 0
for i in a:
    if i in b:
        e += 1
    if i in c:
        d += 1
print("vowel:")
print(e)
print("consonant:")
print(d)
