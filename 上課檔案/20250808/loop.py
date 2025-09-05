'''
l = [1 for i in range(6)]
print(l)

l = [int(i) for i in input().split()]
print(l)

a, b, c = [int(i) for i in input().split()]
print(a, b, c)

l = [0 for _ in range(5)]
print(l)
'''
#continue(skip) break(stop)
for i in range(10):
    if i % 3 == 0: continue
    if i == 7: break
    print(i)