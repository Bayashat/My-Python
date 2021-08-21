              ##   1.List Comprehension
## 1) don't use:                                        
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newlist = []                                           
                                                  
for x in fruits:                                        
  if "a" in x:                                         
    newlist.append(x)                                   
        
print(newlist)                                          
---------------------------------------------------------
              ## 2) Uses:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)  # ['apple', 'banana', 'mango']
--------------------------------------------------------------------------------------------------------------

                ##   3.The Syntax
newlist = [expression for item in iterable if condition == True]

------------------------------------------------------------------------------------------------------------
                ##   4.Condition
The condition is like a filter that only accepts the items that valuate to True.
With no if statement:

newlist = [x for x in fruits]
--------------------------------------------------------------------------------------------------------
                ##   5.Iterable
The iterable can be any iterable object, like a list, tuple, set etc.

Example：
newlist = [x for x in range(10)]

Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]
----------------------------------------------------------------------------------------------------------------
                ##   6.Expression
1.Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
You can set the outcome to whatever you like:

2.Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

3.Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
-----------------------------------------------------------------------------------------------------------------