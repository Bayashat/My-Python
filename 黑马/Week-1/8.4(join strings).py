#语法： my_str.join(可迭代对象) ： 将 my_str 这个字符串添加到可迭代对象的两个元素之间
# 可迭代对象: str,列表(需要列表中的每一个数据都是字符串)
#返回值：一个新的字符串

my_str = '-'.join('hello') # 会把_加入到hello每两个元素之间， 即
print(my_str)  # h_e_l_l_o
print('_*_'.join('hello')) # h_*_e_*_l_*_l_*_o

# 定义个列表:
my_list = ['hello', 'cpp','python']
print('_'.join(my_list))  # hello_cpp_python
