import numpy as np

a=np.arange(0.4,0.8,0.1)
print(a)
a=np.arange(0.5,0.8,0.1)
print(a)
a=np.arange(0.5,0.75,0.1)
print(a)
# Arange is not good for floating

a=np.linspace(0.5,0.7,3)
print(a)
#np.linspace(start,stop,num/step)



#ArrayIndexing

a=np.arange(1,6)
print(a)

b=a[1]
print(b)

c=a[2:4]
print(c)

d=a[-2:]
print(d)

e=a[::2]
print(e)

f=a[[1,3,4]]
print(f)

a[2:4]=0
print(a)

#'//'--->integer division
#'**'---> exponetial function