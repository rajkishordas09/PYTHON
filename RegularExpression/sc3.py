import re

txt = "The rain in Spain aindi"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)#not st with ain in word
y = re.findall(r"ain\B", txt)#not end with ain in word

print(x)
print(y)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")