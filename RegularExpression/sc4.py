import re

txt = "The rain345 in Spain567"

#Check if the string contains any digits 
# (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
