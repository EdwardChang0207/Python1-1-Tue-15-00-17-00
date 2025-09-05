name = ['kevin', 'andy', 'mary']
score = [60, 100, 8]
'''

print(name[0],'的成績是：',score[0],'分', sep='')
print(name[1],'的成績是：',score[1],'分', sep='')
print(name[2],'的成績是：',score[2],'分', sep='')

(1)%
%s -> str
%d -> int
%f -> float
(2).format
(3)f-string
'''
print('%6s的成績是:%3d分'%(name[0],score[0]))
print('{:6s}的成績是:{:3d}分'.format(name[1],score[1]))
print(f'{name[2]:6}的成績是:{score[2]+10:3}分')

pi = 3.1415926
print(f'{pi:5.2f}')