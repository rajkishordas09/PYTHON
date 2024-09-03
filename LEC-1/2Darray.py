import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)

b=a[1,2]#[row,column]
print(b)

c=a[1,:]
print(c)

d=a[:,2]
print(d)

e=a[:,1:3]
print(e)

f=a[-2:,-2:]
print(f)

g=a[::2,1::2]
print(g)



a=np.zeros((3,2))
print(a)#3-rows ,2-columns

a=np.eye(3,3)#identity matrix
print(a)


