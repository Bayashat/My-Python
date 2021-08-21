thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# 字典 dict 使用 {} 定义，是由键值对组成的(key-value)
# 变量 = {key1:value1, key2:value2,...}
# key 可以是字符串类型和数字类型(int,float),不能是列表
# value值可以是任何类型
-------------------------------------------------------------------------------------------------------
#   1.Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
-------------------------------------------------------------------------------------------------------------------
#   2.Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # "Ford"
----------------------------------------------------------------------------------------------------------------------------
#   3.Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
-------------------------------------------------------------------------------------------------------------------------------
#   4.Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
-----------------------------------------------------------------------------------------------------------------------------
#   5.Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
-------------------------------------------------------------------------------------------------------------------------
#   6.Dictionary Length
use the len() function:

print(len(thisdict))  # 3
------------------------------------------------------------------------------------------------------------------------------\
#   7.dictionary Items - Data Types
The values in dictionary items can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
---------------------------------------------------------------------------------------------------------------------------
#   8.type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
--------------------------------------------------------------------------------------------------------------------------------
#   9.Create empty dict:
d = {}
d = dict()