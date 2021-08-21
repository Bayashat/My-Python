import re 

txt = 'The rain in Ilaty'
x = re.search('The', txt)
print(x)    # <re.Match object; span=(0, 3), match='The'>