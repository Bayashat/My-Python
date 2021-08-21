#   Once a set is created, you cannot change its items, but you can add new items
---------------------------------------------------------------------------------------------------------

                    ##   1.add() method ： 只添加单一数据

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

------------------------------------------------------------------------------------------------------

                    ##   2.Update()-1 : 增加序列数据, 不支持加单一数据
To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)  # {'apple', 'mango', 'papaya', 'cherry', 'pineapple', 'banana'}

----------------------------------------------------------------------------------------------------------

                    ##   3.Update()-2 : Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)  # {'banana', 'cherry', 'apple', 'kiwi', 'orange'}


thisset.update([10,20,30])

print(thisset)  # {10, 'orange', 'cherry', 'apple', 'banana', 20, 'kiwi', 30}

--------------------------------------------------------------------------------------------------------