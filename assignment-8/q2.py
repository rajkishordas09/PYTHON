def A(n):
    if n<10:
        return n 
    return n%10+A(n//10)   

n=1234
print(A(n))
