import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print("The first white-space character is located in position:", x.start()) 
print("The first white-space character is located in position:", x.end()) 
print(type(x.end()))