                ### 需要将 0-10 数放入列表
                ## <1> Simple List 推导式
# 1. Use while loop:
list1 = []
i=0
while i<11:
    list1.append(i)
    i+=1
print(list1)    # [0,1,2,3,4,5,6,7,8,9,10]

# 2. Use for loop:
list1 = []
for i in range(10):
    list1.append(i)
print(list1)     # [0,1,2,3,4,5,6,7,8,9,10]

# Use List 推导式:
list1 = [i for i in range(10)]
print(list1)
----------------------------------------------------------------------------------------------------------

            ## <2> Conditional List 推导式
# need a list with even numbers between 0-10

# Method-1: Range steps:
list1 = [i for i in range(0, 10, 2)]
print(list1) 

# Method-2: Use IF:
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

--------------------------------------------------------------------------------------------------------------
            ## <3> Multiple FOR List 推导式:
# Need create such List:
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)