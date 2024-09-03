def test1():
 test1.a = 10
 b=1
 print(type(test1.a))
 print('inside function test1 ', test1.a, b)
 def test2():
   b=5
   test1.a = 8
   print('Inside function test2 ', test1.a, b)
 test2()
 print('Outside function test2 ', test1.a, b)
test1()
print(type(1))