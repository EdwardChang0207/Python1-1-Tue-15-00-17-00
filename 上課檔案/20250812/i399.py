a = [int(i) for i in input().split()] #['a1','a2',"a3"]
#sort() -> loop throgh a -> amount >= 2? -> P
a.sort()
for i in range(len(a)):#[2,2,3]
    P = a.count(a[i])
    if P >= 2:
        x = a[i]
        break
#remove(item)*P-1
for i in range(P-1):
    a.remove(x)
#reverse()
a.reverse()
print(P,*a)