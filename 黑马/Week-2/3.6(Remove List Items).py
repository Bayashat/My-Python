my_list = [1,2,3,4,5,6,7]

                ##   1.Remove.(): 根据元素的数据值删除,直接删除原列表中的数据
my_list.remove(4)
print(my_list)   # [1,2,3,5,6,7]
------------------------------------------------------------
                ##   2.pop(index) : 根据下标删除，默认删除最后一个数据，返回删除内容
xxx = my_list.pop()

print(xxx) # 7
print(my_list) # [1,2,3,5,6]

yyy = my_list.pop(1)

print(yyy) # 2
print(my_list)   # [1,3,5,6]
--------------------------------------------------------------
                ##   3.del keyword : del 列表[index] ：同样可以按下标删除 + 还能删除列表
The del keyword can also delete the list completely: 
Can write as : del 目标, or del(目标)

del my_list[2] 
print(my_list) # [1,3,6]

thislist = ["apple", "banana", "cherry"]
del thislist
------------------------------------------------------------
                ##   4.Clear the List
The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []
------------------------------------------------------------------