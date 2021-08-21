            ## <1> key值查找
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name']) # Tom
print(dict1['id']) # 报错
# 如果当前查找的key存在，则返回对应的值；否则则报错。

            ## <2> get()
# 语法: dict.get(key,value)
# 注意：如果当前查找的key不存在则返回第二个参数(默认值)，如果省略略第二个参数，则返回 None。
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name')) # Tom
print(dict1.get('id', 110)) # 110
print(dict1.get('id')) # None

            ## <3> keys()  返回可迭代对象 , 也就是所有的key
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])

            ## <4> values()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.values()) # dict_values(['Tom', 20, '男'])

            ## <5> items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key, 2 是value
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items()) # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])