import re
txt = "heaaaaaao planet heo hoe"

#Search for a sequence that starts with "he",
#  followed by 0 or more  (any) characters,
#  and an "o":

x = re.findall("he.*o", txt)#unlimited character or 0
y = re.findall("hea*o", txt)
print(x)
print(y)
