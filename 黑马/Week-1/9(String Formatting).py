                            ## 1.String format()
# The format() method allows you to format selected parts of a string.
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
price(txt.format(price))  #  The price is 49.00 dollars
----------------------------------------------------------------------------------------------
                            ## 2.Multiple Values
# If you want to use more values, just add more values to the format() method:
# And add more placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
--------------------------------------------------------------------------------------------
                            ## 3.Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
-------------------------------------------------------------------------------------------
                            ## 4.Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
#  but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
