my_str = 'hello world itcast and itcastcpp'
                                ## 1.Upper Case

# The "upper()" method returns the string in upper case:
print(my_str.upper())
---------------------------------------------------------------------------------------------------------------
                                ## 2.Lower Case

# The "lower()" method returns the string in lower case:

----------------------------------------------------------------------------------------------------------------------
                                ## 3.Replace String-1 : 替换字符串中的字符

# The replace() method replaces a string with another string:
print(my_str.replace("h", "j"))

----------------------------------------------------------------------------------------------------------------
                                ## 4.Replace String-2 ： 替换字符串,将 my_str 中的 old_str 替换成 new-str
# my_str.replace(old_str, new_str, count)
# old_str: 将要被替换的字符串
# new_str: 新的，替换成的字符串
# count: 替换的次数， 默认 全部替换
# 返回值： 得到一个新的字符串，不会改变原来的字符串
my_str1 = my_str.replace('itcast','itheima')
print(my_str1) # 'hello world itheima and itheimacpp'
my_str2 = my_str.replace('itcast','itheima',1) # 仅替换一次
print(my_str2) #'hello world itheima and itcastcpp'

---------------------------------------------------------------------------------------------------------------------
                                ## 5.Split String-切割字符串
# 语法: my_str.split(sub_str, count) 将my_str字符串按照sub_str 进行切割,并存入一个list
# sub_str: 按照什么内容切割字符串, 默认是空白字符，空格，
# count : 切割几次， 默认是 全部切割
# 返回值: 列表 []
result = my_str.split() # 按照空白字符，全部切割  # ['hello','world','itcast','and','itcastcpp']
print(my_str.split('itcast'))  # ['heelo world','and','cpp']
print(my_str.split('itcast',1)) # 切割1次  # ['heelo world','and itcastcpp']
print(my_str.rsplit('itcast',1)) # 从后面切割1次  # ['heelo world itcast and','cpp']