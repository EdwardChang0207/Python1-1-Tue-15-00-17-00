#數學運算 num op num -> num
# print(2**3) #2*2*2 -> 2的3次方
# print(20%6) #20/6 = 3(商)...2(餘)
# print(20//6)
#邏輯運算 
#(1)num op num -> bool
# print(1 > 2)
# print(1 >= 2)
# print(1 < 2)
# print(1 <= 2)
# print(1 == 2)
# print(1 != 2)
#(2)bool op bool -> bool
'''
1. not 反閘 
周杰倫:哎呦不錯喔
不(not)錯(False) -> True
錯 -> False
不(not)行(True) -> False
行 -> True
print(not False)

2. or 或閘
math or english -> 3000
T.       F.        T
F.       T.        T
T        T.        T
F.       F.        F
a, b = False, False
print(a or b)

3. and 且閘
打掃 and HW -> :)
T.      F.    F
F.      T.    F
T.      T.    T
F.      F.    F
a, b = False, False
print(a and b)

4. xor (excursive or) 斥或閘
珍奶 xor 烏龍 -> :)
T.       F.     T
F.       T.     T
T.       T.     F
F        F.     F
a, b = True, False
(1)not or and
print((a or b) and not(a and b))
(2)binary
print(a^b)
'''

# (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

'''
運算子 operator
運算元 operatee
'''

x = 1
# x(new) = x(old) + 1
x = x + 1
print(x)
x += 1
print(x)