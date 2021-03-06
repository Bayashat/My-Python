###  2 reduce()
reduce(func(x,y)，lst)，其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累积计算。
注意：reduce()传⼊的参数func必须接受2个参数。

# 需求：计算list1 序列中各个数字的累加和。

import functools

list1 = [1, 2, 3, 4, 5]

def func(a, b):
    return a + b

result = functools.reduce(func, list1)
print(result) # 15