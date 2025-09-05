'''
l = []
print(bool(l))
if l:
    print('hi')
else:
    print('hello')

l = [i for i in range(10)]
print(l[1:len(l):2])
'''

#len -> length 長度
'''
l = [1,2,3]
l.append(4)
print(l)

l = [1,1,1,2,2,3,3,3,3,4]
print(l.count(1))
print(l.count(3))

l = [1,2,3,1,1]
print(l.index(1))

l = [1,2,3]
l.insert(0,4)
print(l)

l = [1,2,3]
a = l.pop(0)
print(a)
print(l)

l = [1,2,3]
l.remove(1)
print(l)

l = [1,2,3]
l.reverse()
print(l)

l = [3,2,1]
l.sort()
print(l)
l = [0,1,2,3,4]
len(l) -> 5

for i in range(len(l)) -> 0~4
    l[i]
'''