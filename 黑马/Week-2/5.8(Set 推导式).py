# Need: Create a set with square of this list:
list1 = [1,1,2]

# Solution: 
list1 = [1, 1, 2]

set1 = {i ** 2 for i in list1}

print(set1)  # {1, 4}
# 集合有去重功能