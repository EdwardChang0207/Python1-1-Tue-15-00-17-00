n = int(input())
a, b, c = 0, 0, 0
#重複判斷n個數字
for i in range(n):
    # 判斷數字對3取餘數的結果
    x = (int(input()) % 3)
    if x == 0: a += 1 
    elif x == 1: b += 1
    else: c += 1

#輸出答案
print(a,b,c)
