n=int(input())
s=[int(i)for i in input().split()]
s.sort()
print(*s)
if s[0]>=60:
    print('best case')
    print(s[0])
elif s[-1]<60:
    print(s[-1])
    print('worst case')
else:
    for Q in range(len(s)-1,-1,-1):
        if s[Q]<60:
            print(s[Q+1])
            print(s[Q])
