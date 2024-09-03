def are_anagrams(str1, str2):
   str1=str1.replace(" ","").lower()
   str1=str2.replace(" ","").lower()

   return sorted(str1)==sorted(str2)

str1='jdfrtryfhk'
str2='abc'
a=are_anagrams(str1, str2)
print(a)