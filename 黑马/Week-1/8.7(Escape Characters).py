# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."  #We are the so-called "Vikings" from the north.

# Other escape characters used in Python:

        \(在行尾时)	        续行符

>>> print("line1 \
... line2 \
... line3")
line1 line2 line3
>>>

        \\ 反斜杠符号	        Backslash
>>> print("\\")
\

        \'	    单引号       Single Quote
>>> print('\'')

'

        \"	    双引号
>>> print("\"")
"

        \a	    响铃

>>> print("\a")
执行后电脑有响声。

        \b	    退格(Backspace)
>>> print("Hello \b World!")
Hello World!

        \000	空
>>> print("\000")
>>>

        \n	    New Line    换行
>>> print("\n")


>>>

        \v	纵向制表符
>>> print("Hello \v World!")
Hello
       World!
>>>

            \r	     Carriage Return    \r	回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
>>> print("Hello\rWorld!")
World!
>>> print('google runoob taobao\r123456')
123456 runoob taobao

        \t	    Tab   横向制表符
>>> print("Hello \t World!")
Hello      World!
>>>

        \f	    Form Feed   换页
>>> print("Hello \f World!")
Hello
       World!
>>>

\yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。	
>>> print("\110\145\154\154\157\40\127\157\162\154\144\41")
Hello World!

\xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
>>> print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
Hello World!


\ooo	        Octal value
\xhh	        Hex value

\other	其它的字符以普通格式输出
