'''
print(1)
print(2)
print(3)
...
'''

# while <condition>:bool:
#     ...
'''
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
while True:
    print(1)
'''

#for index in <range>:
'''
for sushi in ['鮭魚','鮪魚','玉子燒']:
    if sushi == '鮭魚':
        print(sushi)
    else:
        print('pass')

for i in 'hello':
    print(i)
'''

#range(start[init:0], end, interval[init:1])
#from start, to end-1, += interval each time
'''
for i in range(0, 10, 2):
    print(i)
'''
'''
for i in range(1, 5):
    print(i)
'''
'''
for i in range(3):
    print(i)
'''

#1 ~ 10
for i in range(1, 11):
    print(i, end=' ')
print()   
#10 ~ 1
for i in range(10, 0, -1):
    print(i, end=' ')
print()   
#1, 3, 5, ..., 27
for i in range(1, 28, 2):
    print(i, end=' ')
print()
#20, 16, 12, ..., 0
for i in range(20, -1, -4):
    print(i, end=' ')
print()