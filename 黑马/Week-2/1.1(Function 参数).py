                            ##  1.Arguments  位置参数

# 传递和定义参数的顺序及个数必须一致。
Arguments are often shortened to "args" in Python documentations.

def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20, '男')  # 您的名字是TOM, 年龄是20, 性别是男
-----------------------------------------------------------------------------------------------------------------------

                                ##  2.Keyword Arguments  关键字参数
# 函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')

user_info(name='Rose', age=20, gender='female')  # 您的名字是Rose, 年龄是20, 性别是female

# 注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序.
user_info('Rose', age=20, gender='女')  # 您的名字是Rose, 年龄是20, 性别是女. 
user_info('⼩明', gender='男', age=16)  # 您的名字是⼩明, 年龄是16, 性别是男.

The phrase Keyword Arguments are often shortened to "kwargs" in Python documentations.
-------------------------------------------------------------------------------------------------------------

                        ##  5.Default Parameter Value  缺省参数
#  缺省参数也叫默认参数，⽤于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 调用函数时，缺省参数的值如果没有传入,则取默认值.
# (注意：所有位置参数必须出现在默认参数前，包括函数定义和调⽤)
If we call the function without argument, it uses the default value:

def user_info(name, age, gender='男'):
    print(f'您的名字是{name}, 年年龄是{age}, 性别是{gender}')


user_info('TOM', 20)  # 您的名字是TOM, 年龄是20, 性别是男
user_info('Rose', 18, '⼥')  # 您的名字是Rose, 年龄是18, 性别是⼥

# 注意：函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值。
-------------------------------------------------------------------------------------------------------------------

                        ##  6.Arbitrary Arguments, *args  不定长参数之包裹位置传递
# 不定长参数也叫可变参数。⽤于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得⾮常⽅便。
# * 包裹位置传递 : 接受所有位置参数，返回一个元组
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # The youngest child is Linus

def user_info(*args):
    print(args)

user_info('TOM')  # ('TOM',)
user_info('TOM', 18)  # ('TOM', 18)
# 注意：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是包裹位置传递。

------------------------------------------------------------------------------------------------------------------------

                        ##  7.Arbitrary Keyword Arguments, **kwargs.  不定长参数之包裹关键字传递
# 包裹关键字传递 : 收集所有关键字参数,返回一个字典
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

def user_info(**kwargs):
    print(kwargs)

user_info()  # {}  返回了空字典
user_info(name='TOM')  # {'name': 'TOM'}
user_info(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}

# 综上：⽆论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。
Arbitrary Kword Arguments are often shortened to "**kwargs" in Python documentations.
------------------------------------------------------------------------------------------------------------------------

                            ## 6 and 7 的小总结
# 在形参前边加上一个 * ， 该形参变为不定长元组形参，可以接受所有的位置实参，类型是元组.
# 在形参前边加上两个 ** ， 该形参变为不定长字典形参，可以接受所有的关键字实参，类型是字典.

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5) {}
func(a=1, b=2, c=3, d=4)  # () {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(1, 2, 3, a=4, b=5, c=6)  # (1, 2, 3) {'a': 4, 'b': 5, 'c': 6}

---------------------------------------------------------------------------------------------------------------
                            ## 8.函数形参的完整格式
#  普通形参(a)   缺省形参(b)   不定长元组形参(*args)   不定长字典形参(**kwargs)

# 1)
def func(a, b=1):   # 先普通，再缺省
    pass

def func1(a,b=1, *args ): # 语法没有错误，但是缺省参数不能使用默认值
    print('a',a)
    print('b', b)
    print(args)
func1(1,2,3,4)  #  a 1   b 2    (3,4)

# 2)
def func2(a, *args, b=1 ):  # 普通形参，不定长元组形参  缺省形参
    print('a',a)
    print('b', b)
    print(args)
func2(1,2,3,4)  #  a 1    b 1    (2,3,4)
func2(1,2,3,4,b = 10)  #  a 1    b 10    (2,3,4)

# 3)
def func3(a, *args, b=1 , **kwargs):  # 普通形参，不定长元组形参  缺省形参  不定长字典形参
    print('a',a)
    print('b', b)
    print(args)

