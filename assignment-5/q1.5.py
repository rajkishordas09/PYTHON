a = 4
def f():
  # nonlocal a
 a = 5
 def g():
   #nonlocal a
   a = 10
   print('Inside function g, ', 'a=', a)
   def h():
    nonlocal a
    a = 20
    print('Inside function h, ', 'a=', a)
   h()
   print('Inside function g, ', 'a=', a)
 g()
 print('Inside function f, ', 'a=', a)#print non local term
print('outside function f, ', 'a=', a)#print non local term
f()
print('Inside function f, ', 'a=', a)