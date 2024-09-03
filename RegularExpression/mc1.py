# "[a-m]"=A set of characters
import re
t='''Once upon a time there was an old mother pig
 who had three little pigs and not enough food to 
 feed them. So when they were old enough,
  she sent them out into the world to seek their
   fortunes.'''

f=re.findall("[a-m]",t)   
print(f)