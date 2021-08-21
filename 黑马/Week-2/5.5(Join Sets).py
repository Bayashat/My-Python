                    ##   1.Join Two Sets
You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
---------------------------------------------------------------------------------------------------------
                    ##   2.Union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
---------------------------------------------------------------------------------------------------------------
                ##   3.Update()
The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
-----------------------------------------------------------------------------------------------------
######   Note: Both union() and update() will exclude any duplicate items.
-------------------------------------------------------------------------------------------------
                ##   4.Keep ONLY the Duplicates-1
The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
-----------------------------------------------------------------------------------------------------------
                ##   5.Keep ONLY the Duplicates-2
The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
------------------------------------------------------------------------------------------------------------------
                ##   6.Keep All, But NOT the Duplicates-1
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
-----------------------------------------------------------------------------------------------------------------------
            ##   7.Keep All, But NOT the Duplicates-2
The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
---------------------------------------------------------------------------------------------------------------------------