                            # <1> 普通输出:
print("hello world")

#To combine both text and a variable, Python uses the + character:

x = "awesome"
print("Python is " + x) # Python is awesome

# You can also use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z) # # Python is awesome
-----------------------------------------------------------------------------------------------------------------------

                            # <2> 格式化输出:
age = 18
print("my age is %d" % age) # my age is 18

name = 'issac'
height  = 170.5
print('my name is %s, my age is %d , height is %.2f' %(name, age,height)) #想让小数只保留小数点后2位的话写: %.2f
# my name is issac, my age is 18 , height is 170.50

index = 1
index2 = 1000

# %06d  表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
print('my index is %03d' % index) # 001
print('my index is %03d' % index2) # 1000

---------------------------------------------------------------------------------------------------------------------
#       <1>使用格式化输出时，想输出2个百分号就要写 2个%:
print('PASS is %d%%' %50)   # PASS is 50%

#       <2> 从python 3.6版本开始支持f-string, 占位统一使用{},填充的数据直接写在{}里面
#  语法: f'{表达式}
age = 18
name = 'issac'
print(f"my name is {name}, my age is {age}") # my name is issac, my age is 18

height = 170.5
# 默认是本来几位，就显示几位
print(f"my tall is {height}cm") # 170.5
# 指定显示2位:
print(f"my tall is {height:.2f}cm") # 170.50
---------------------------------------------------------------------------------------------------------------------------
                                # <3> 拓展格式化字符串 : actually you can use %s for all!
age = 18
name = 'issac'
height  = 170.5
print('my name is %s, my age is %s , height is %s' %(name, age,height)) #同样显示 my name is issac, my age is 18 , height is 170.5

----------------------------------------------------------------------------------------------------
%c ------- 字符
%s ------- 字符串
%d ------- 有符号十进制整数
%u ------- 无符号十进制整数
%o ------- 八进制整数
%x ------- 十六进制整数(小写字母0x)
%X ------- 十六进制整数(大写字母0x)
%f ------- 浮点数
%e ------- 科学计数法(小写e)
%E ------- 科学计数法(大写e)
%g ------- %f 和 %e 的简写
%G ------- %f 和 %E 的简写

---------------------------------------------------------------------------------------------------
            # <4.1> 转义字符: \n : 换行输出，
在输出的时候，如果有 \n , 那么此时\n 后的内容会在另一行显示

print("123456789-------") # 会在一行显示
print("123456789\n---------") # 一行显示123456789， 另外一行显示--------

# print 函数输出之后，默认会添加一个换行，如果不想要这个换行可以去掉
print("hello", end= ' ')

-------------------------------------------------------------------------------------------------------------
    # <4.2> 转义字符 : \t : 制表符，一个tab键(4个空格)的距离
print('\tabcd') # '    abcd' 

-----------------------------------------------------------------------------------------------------------------
#   < 4.3>  结束符

想一想，为什么两个print会换行输出？
在Python中，print()， 默认⾃自带end="\n" 这个换行结束符，所以导致每两个print 直接会换⾏展示，用户可以按需求更改结束符。
print('hello', end = '\n')  #
print('world', end = '\t')
print('hello' end = '...')
print('python')

# 输出结果:
'''
hello
world   hello...python
'''
---------------------------------------------------------------------------------------------