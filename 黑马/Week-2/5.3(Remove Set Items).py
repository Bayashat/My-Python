------------------------------------------------------------------------------------------------------
                ##   <1> Remove() ： 删除集合中的指定数据，如果数据不存在则报错
thisset = {10，20，30，40，50}

thisset.remove(10)
print(thisset) # {20，30，40，50}

thisset.remove(100) # Error

------------------------------------------------------------------------------------------------------
                ##  <2> discard() : 删除集合中的指定数据，如果数据不存在也不会报错
thisset = {10,20,30,40,50}

thisset.discard(10)
print(thisset)  # {20,,30,40,50}

thisset.remove(100) 
print(thisset) # 20,30,40,50

####  Note: If the item to remove does not exist, discard() will NOT raise an error.
-------------------------------------------------------------------------------------------------------------------
                #   <3>.pop() ： 随机删除集合中的某个数据，并返回这个数据.
# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

thisset = {10,20,30,40,50}
x = thisset.pop()

print(x)    # 40

print(thisset) # 10,20,30,50
--------------------------------------------------------------------------------------------------
                #   3.clear()
The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
--------------------------------------------------------------------------------------------------------
                #   4.del()
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
-------------------------------------------------------------------------------------------------------