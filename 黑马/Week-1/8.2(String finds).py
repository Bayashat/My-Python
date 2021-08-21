my_str = 'hello world itcast and itcastcpp'

                        # <1> Find : 检测 str 是否包含在my_str 中，如果是，返回开始的索引值，否则返回-1
# 语法: my_str.find(sub_str,start,end)
# sub_str: 要在字符串中查找的内容，类型str
# start: 开始位置，从哪里开始查找，默认是0
# end : 结束位置，查找到哪里结束，默认是 len()

print(my_str.find('hello')) # 0
print(my_str.find('itcast')) # 12
# 从下标为3的位置开始查找
print(my_str.find('hello',3)) # -1
--------------------------------------------------------------------------------------------------
                            # <2> rfind : Right Find : 从右边(后边)开始查找:
print(my_str.rfind('itcast'))  # 23
-------------------------------------------------------------------------------------------------
                            # <3> index(): 作用和 find() 一模一样， 唯一的区别是: 若没有找到，会报错
# 它也有叫 rindex() 的，也是从右边(后面)开始查找
-----------------------------------------------------------------------------------------------------
                            # <4> Count(sub_str,start,end):统计出现的次数:
print(my_str.count('aaaa')) # 0
print(my_str.count('hello')) # 1
print(my_str.count('itcast')) # 2
print(my_str.count('itcast',20)) # 1