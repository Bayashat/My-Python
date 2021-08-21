          ##   1.POP() : dict.pop(key) ： 按key值删除，返回值是删除的key对应的value.
The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
result = thisdict.pop("model")  # 可以将删除的value接受
print(result) # "Mustang"

--------------------------------------------------------------------------------------------------

            ##   2.popitem()
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang'}

----------------------------------------------------------------------------------------------
            ##   3."del" keyword-1 ：del dict[key]  根据key值删除数据
The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 
---------------------------------------------------------------------------------------------------------
              ##   4."del" keyword-2 : del 字典名: 直接将这个字典删除了. 后面的代码不能再直接使用这个变量了，除法再次定义.
The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict  # or:  del(thisdict)
print(thisdict) # Error
------------------------------------------------------------------------------------------------------------------
            ##   5.The clear() method empties the dictionary: 清空，删除所有的键值对

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # {}
----------------------------------------------------------------------------------------------------------------------