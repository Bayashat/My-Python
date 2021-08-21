                  ##   1.Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
----------------------------------------------------------------------------------------------------------------
                  ##   2.Negative Indexing
-1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
-----------------------------------------------------------------------------------------------------------------------
                  ##   3.Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
---------------------------------------------------------------------------------------------------------------------------
                  ##   4.Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
-------------------------------------------------------------------------------------------------------------------------------
                  ##   5.Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
----------------------------------------------------------------------------------------------------------------------------------
                  ##   6.Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example
Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
--------------------------------------------------------------------------------------------------------------------------------------
#   7.Add Items
Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
------------------------------------------------------------------------------------------------------------------------------------------
#   8.Remove Items
Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
------------------------------------------------------------------------------------------------------------------------------------
#   9.Delete Items
The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
-------------------------------------------------------------------------------------------------------------------------------