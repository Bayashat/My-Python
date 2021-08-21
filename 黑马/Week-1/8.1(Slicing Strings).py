                            ## 1. Slicing  提取字符串

# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])   # ll0
--------------------------------------------------------------------------------------------------------
                            ## 2.Slice From the Start 从起始位置提取到...
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5]) # Hello
----------------------------------------------------------------------------------------------------------------
                            ## 3.Slice To the End
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) # llo, World!
----------------------------------------------------------------------------------------------------------
                            ## 4.Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2]) # orl

-----------------------------------------------------------------------------------------------
                            ## 5.字符串快速逆置：
s = 'hello'
print(s[::-1]) # olleh
-----------------------------------------------------------------------------------------------
                            ## 6.得到和原来一样的字符串:
a = s[:]
print(a) # hello