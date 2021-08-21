"""
向列表中添加数据的方法，都是直接在原列表中进行添加的，不会返回新的列表.
可变
"""

a = list(input().split())
                ##   1.Append Items : 向列表尾部追加数据
# 如果追加的数据是一个序列，则追加整个序列到列表

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ["apple", "banana", "cherry"， "orange"]

thislist.append([11,22])
print(thislist) # ["apple", "banana", "cherry"， "orange",[11,22] ]

----------------------------------------------------------------------------

                ## 2.Insert Items : list.insert(下标，数据) ： 在指定的下标位置前进行添加数据
The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']

----------------------------------------------------------------------------

                ## 3.Extend List：列表.Extend(可迭代对象) # str和list . 会将可迭代对象中的数据逐个添加到原列表的末尾.
# 若追加数据是list,会逐一添加
Add the elements of "tropical" to "thislist":

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

my_list = [1,'issac',2]
my_list.extend('hel')
print(my_list)  # [1, 'issac', 2, 'h', 'e', 'l']  # 会将序列(可迭代对象)拆开加入

--------------------------------------------------------------------------------
                ## 4.Add Any Iterable
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
--------------------------------------------------------------------------------