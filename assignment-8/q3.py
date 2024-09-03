def A(a,b):
    if b==0:
        return 1
    return a*A(a,b-1)   

a=2
b=3
print(A(a,b))
