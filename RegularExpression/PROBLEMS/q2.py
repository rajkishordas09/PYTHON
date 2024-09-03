# Write a Python program that matches a string 
# that has an a followed by zero or more b's.
import re
def A(s):
  a=re.findall("\b*",s)
  return a
print(A("raj bb ab ababb"))

 