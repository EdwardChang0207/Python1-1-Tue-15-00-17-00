l = input().split() #'1 1' -> ['1', '1']
m, d = int(l[0]), int(l[1])
s = (m*2+d)%3

#sol1
'''
if s == 0: print('普通')
elif s == 1: print('吉')
else: print('大吉')
'''
#sol2
lucky = ['普通','吉','大吉']
print(lucky[s])