import re
# "." -->	Any character (except newline character)
txt = "hello planet hemao heado"

#Search for a sequence that starts with "he",
#  followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
