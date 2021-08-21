# !!! Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

              ## 1.Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
--------------------------------------------------------------------------------------------------------
              ## 2.Access the Elements of an Array
# Get the value of the first array item:
x = cars[0]
-----------------------------------------------------------------------------------------------------------
              ## 3.Modify the value of the first array item:
cars[0] = "Toyota"
--------------------------------------------------------------------------------------------------------------
              ## 4.The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
x = len(cars)
------------------------------------------------------------------------------------------------------------
              ## 5.Looping Array Elements
for x in cars:
  print(x)
------------------------------------------------------------------------------------------------------------    
              ## 6.Adding Array Elements
cars.append("Honda")
----------------------------------------------------------------------------------------------------------.
                ## 7.Removing Array Elements
# Delete the second element of the cars array:
cars.pop(1)

# You can also use the remove() method to remove an element from the array.
cars.remove("Volvo")
---------------------------------------------------------------------------------------------------------
            ## 8.Array Methods
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
----------------------------------------------------------------------------------------------------------
