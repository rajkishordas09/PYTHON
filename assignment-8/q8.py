def A(n,a=2):
    if n<=1:
        return False
    if n==2:
        return True
    if n%a==0:
        return False
    if a*a>n:
        return True    
    return A(n,a+1)
n=3
print(A(n))
