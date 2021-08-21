### Tuple的元素不能修改
mytuple = ("apple", "banana", "cherry")

                    ##   1. tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
-------------------------------------------------------------------------------------------------
                    ##   2.Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
-------------------------------------------------------------------------------------------------
                    ##   3.Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

                    ##   4.Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

                    ##   5.Allow Duplicates
Since tuple are indexed, tuples can have items with the same value:
-----------------------------------------------------------------------------------------------------------------------------
                    ##   6.Tuple Length
use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
------------------------------------------------------------------------------------------------------------------------
                    ##   7.Create Tuple With One Item
To create a tuple with only one item, you have to add a "comma" after the item

thistuple = ("apple",)  # 定义一个元组时要加逗号
print(type(thistuple))

tuple2 = (10)  # int类型
------------------------------------------------------------------------------------------------------------------------------
                    ##   8.Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")
------------------------------------------------------------------------------------------------------------------------------------
#   9.type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':
<class 'tuple'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
-----------------------------------------------------------------------------------------------------------------------------------------
#   10.The tuple() Constructor
Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
-----------------------------------------------------------------------------------------------------------------------------------------
#   12.Create empty tuple:
t = tuple()
t2 = ()
