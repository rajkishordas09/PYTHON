def A(n):
    if n==0:
        return 0
    return 1/(2**(n-1))+A(n-1)

n=4
print(A(n))
