import re

txt = "hello planet heo"

#Search for a sequence that starts with "he",
#  followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)
y = re.findall("he..?o", txt)

print(x)
print(y)
