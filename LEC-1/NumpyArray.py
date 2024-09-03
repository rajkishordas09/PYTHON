import numpy as np
a=np.arange(6)
print(a)#output in arrayList
#NumpyArray are faster and Compact than PythonList
#size fix
a=np.array([1.,2.,3.,4.])
print(a)    
a=np.zeros(3,str)
print(a)
a=np.zeros(3,int)
print(a)

a=np.zeros_like(a)
print(a)



a=np.ones(4)
print(a)
a=np.ones_like(a)
print(a)


a=np.empty(5)
print(a)
a=np.empty_like(a)
print(a)

a=np.full(3,7)
print(a)
a=np.full_like(a,7)
print(a)


