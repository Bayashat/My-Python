# list.sort() : 默认从小到大排序
                  ##   1.Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

---------------------------------------------------------------------------------

                  ##   2.Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

------------------------------------------------------------------------------------------

                  ##   3.Sort Descending : 若想从大到小排序，使用: list.sort(reverse=True)
# 语法 ： 列表序列.sort(key=None, reverse=false)
# reverse = True 是降序   reverse = False 是升序

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

-------------------------------------------------------------------------------------------

                  ##  《4》 sorted(list) : 不会在原列表中进行排序，会得到一个新的列表:
my_list = [3,7,4,2,8,5,3]
my_list2 = sorted(my_list) 
print(my_list2) # [2,3,3,4,5,7,8]

my_list2 = sorted(my_list, reverse=True)
print(my_list2) # [[8, 7, 5, 4, 3, 3, 2]]

------------------------------------------------------------------------------------------
                ##   5.Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
----------------------------------------------------------------------------------------------
              ##   6.Case Insensitive Sort
##若不区分大小写会先将大的sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

## Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
----------------------------------------------------------------------------------------
            ##   7.Reverse Order : 会改变原列表

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
-----------------------------------------------------------------------------------------
            ##   8.逆置.[::-1] : get a new list
thislist = [1,2,3,4,5]
xx = thislist[::-1]
print(xx)  # 5,4,3,2,1