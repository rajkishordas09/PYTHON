import re
txt = "The rain5_6 in Spain 123 "

#Return a match at every word character
#  (characters from a to Z, digits from 0-9, 
# and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")