              ##   1.Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
----------------------------------------------------------------------
              ##   2.Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
-----------------------------------------------------------------------
              ##   3.sing a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i+=  1
---------------------------------------------------------------------------
              ##   4.Looping Using List Comprehension
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
----------------------------------------------------------------------------