globalVar = 10
def test():
 global globalVar
 localVar = 20
 globalVar = 30
 print('Inside function test: globalVar =', globalVar)
 print('Inside function test: localVar =', localVar)
print('Outside function test: globalVar =', globalVar) 
test()
print('Outside function test: globalVar =', globalVar)
