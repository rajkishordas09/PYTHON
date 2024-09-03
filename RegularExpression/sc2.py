import re

txt = " ainThe rain in Spain"

#Check if "ain" is present at the end or start of a WORD:

x = re.findall(r"\bain", txt)#start with
y = re.findall(r"ain\b", txt)#ends  with

print(x)
print(y)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")