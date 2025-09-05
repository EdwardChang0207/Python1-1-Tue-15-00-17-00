n = int(input())
c = input().split() #'1 2 3 4 5' -> ['1','2','3','4','5']
t = 0
for i in range(n):
    t += int(c[i])*(i+1)