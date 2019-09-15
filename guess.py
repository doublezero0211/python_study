"""

猜1-100随机数
计算机根据人猜的数字分别给出提示: 大一些/小一些/猜对了

Version: 0.1
Author: Zero
"""
import random

a = random.randint(1,100)
c = 0
while True:
    c+=1
    n = int(input('请输入数字：'))
    if a > n:
        print('大一些')
    elif a < n:
        print('小一些')
    else:
        print('猜对了')
        break
print('你一共猜了%d次'%c)
if c > 7:
    print('你的智商余额不足')
else:
    print('Good!')
