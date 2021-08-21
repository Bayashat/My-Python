## map()
map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/ 迭代器(Python3)返回

# 需求：计算list1 序列中各个数字的2次⽅

list1 = [1, 2, 3, 4, 5]

# 2次方计算的函数
def func(x):
    return x ** 2

# 调用 map
result = map(func, list1)

# or
result = map(lambda x : x**2, list1)

print(result) # <map object at 0x0000013769653198>
print(list(result)) # [1, 4, 9, 16, 25]