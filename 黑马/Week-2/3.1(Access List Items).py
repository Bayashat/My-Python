              ##   1.Access Items
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # "banana"
-------------------------------------------------------------------------------

              ##   2.Negative Indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # "cherry"
------------------------------------------------------------------------------------

              ##   3.Range of Indexes-1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # "cherry", "orange", "kiwi"
-----------------------------------------------------------------------------------

                ##   4.Range of Indexes-2
This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # "apple", "banana", "cherry", "orange"
-------------------------------------------------------------------------------------

                ##   5.Range of Indexes-3
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # "cherry", "orange", "kiwi", "melon", "mango"
------------------------------------------------------------------------------------

                ##   6.Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # "orange", "kiwi", "melon"
----------------------------------------------------------------------------------------

                ##   7.Check if Item Exists
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
-------------------------------------------------------------------------------------------------

                ## 8.与string 不同的是：字符串不能使用下标修改其中的数据， 但是列表可以使用下标修改其中的数据：
lisst = [1,3.14,True]
lisst[1] = 'issac'
print(lisst)  # [1, 'issac', True]