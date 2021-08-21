                        ##   1.Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # "apple", "blackcurran", "cherry"

----------------------------------------------------------------------------------------------
                        ##   2.Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

---------------------------------------------------------------------------------------------------------

                        ##   3.
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

----------------------------------------------------------------------------------------------------------------
                    ##   4.
If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

--------------------------------------------------------------------------------------------------------