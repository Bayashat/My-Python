# 函数就是将一段具有独立功能的代码块 整合到⼀个整体并命名，在需要的位置调用这个名称即可完成对应的需求。
# 函数在开发过程中，可以更高效的实现代码重用

                      ##  1.Creating a Function
def my_function():
  print("Hello from a function")

-------------------------------------------------------------------------------------------------
                      ##  2.Calling a Function
To call a function, use the function name followed by parenthesis:

def my_function():
  print("Hello from a function")

my_function()
-------------------------------------------------------------------------------------------------

                        ##  3.Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.),
and it will be treated as the same data type inside the function.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
'''
apple
banana
cherry
'''
-----------------------------------------------------------------------------------------------------------------
                            ##  4.Return Values

def my_function(x):
  return 5 * x

print(my_function(3))  # 15
-----------------------------------------------------------------------------------------
                            ##  5.The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass
-----------------------------------------------------------------------------------------------
                            ##  6.Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
-----------------------------------------------------------------------------------------------------
                        #  7.
def my_function(x:int):
  print(x)

my_function(3)

def my_function(x:str):
  print(x)

my_function(3)
---------------------------------------------------------------------------------------------------------------
                        ##   8.函数的说明文档:也就是函数的注释，告诉别人，这个函数是干什么的

def 函数名(参数):
  """ 说明文档的位置 """
  代码
  ......

# 查看函数的说明文档:
help(Function name)

-------------------------------------------------------------------------------------------------------------------
                          ##   9. 2 returns:
# 一个函数多个返回值的方法:
def return_num():
  return 1, 2  # 返回tuple
  # 在return后面可以直接写 元组， 列表， 字典， 返回多个值
  return (10,20)
  return [100,200]
  return {'name':'python', 'age': 20}

result = return_num()
print(result)   # (1, 2)

---------------------------------------------------------------------------------------------------------------------
                      ##   10. Don't write return value
def func():
  xxxx
  return    # 返回None , 终止函数运行
