                    #### 0.Python Collections (Arrays)
# There are "4" collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.
----------------------------------------------------------------------------------------------

                    ##  1.List
Lists are used to store multiple items in a single variable.

thislist = ["apple", "banana", "cherry"]
print(thislist)
------------------------------------------------------------------------------------------------
                    ##  2.List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
-------------------------------------------------------------------------------------------------
                    ##  3.List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
----------------------------------------------------------------------------------------------------
                    ##  4.List Items - Data Types
List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
--------------------------------------------------------------------------------------------------
                    ##  5.The list() Constructor
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
------------------------------------------------------------------------------------------------------
                    ##   6.Create empty list:
L = list()

my_list = []