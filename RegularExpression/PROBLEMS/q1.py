# 1. Write a Python program to check that a string contains 
# only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
string="I am a Boy . My age is 22"
s=re.search("[a-zA-Z0-9]",string)
if s:
    print(True)
else:
    print(False)    