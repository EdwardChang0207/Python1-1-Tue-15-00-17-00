s = '1234567'
a = s[0:len(s):2]
b = s[1:len(s):2]
A, B = 0, 0
for i in a:
    A += int(i)
for i in b:
    B += int(i)
print(abs(A-B))