import re

txt = "heo planet hello helllllllo"

#Search for a sequence that starts with "he",
#  followed by 1 or more  (any) characters,
#  and an "o":

x = re.findall("he.+o", txt)

print(x)
