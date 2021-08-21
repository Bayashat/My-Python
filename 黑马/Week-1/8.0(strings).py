                              ## 1.Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

#'hello' is the same as "hello".
--------------------------------------------------
                              ## 2.Assign String to a Variable

a = "Hello"
print(a)
---------------------------------------------------------
                              ## 3.Multiline Strings 多行字符串
# You can assign a multiline string to a variable by using 3 quotes . Or three single quotes:'''
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
-------------------------------------------------------------------
                              ## 4.Strings are Arrays 字符串是数组
# Get the character at position 1 (remember that the first character has the position 0): 获取第一位置的字符.
a = "Hello, World!"
print(a[1])
------------------------------------------------------------------
                              ## 5.Looping Through a String 遍历字符串
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana": # 遍历banana
  print(x)
-----------------------------------------------------------------
                              ## 6.String Length
#To get the length of a string, use the len() function.
#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))   # 12
----------------------------------------------------------------
                              ## 7.Check String
# To check if a certain phrase or character is present in a string, we can use the keyword "in".
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)  # True
------------------------------------------------------
                              ## 8.Use it in an "if statement":
# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")