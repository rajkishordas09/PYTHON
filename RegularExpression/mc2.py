import re

txt = "That will be 59 dollars"

#Find all digit characters in list:\d

x = re.findall("\d", txt)
print(x)
