#   1.Change Values
You can change the value of a specific item by referring to its key name:
dict[key] = value  # 如果key存在，会修改成value, 若key不存在，则会添加这个key和value.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 # 修改
thisdict['name'] = 'issac' # 添加
-----------------------------------------------------------------------------------------------------------
#   2.Update Dictionary
The update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
----------------------------------------------------------------------------------------------------------------
注意 : 在dict int 的1 和 foat 的1 代表一个key值