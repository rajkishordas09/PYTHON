def A(n):
    if n==0:
        return 6
    return (6-n)+A(n-2)   
    # if n==0:
    #     return 0
    # return n+A(n-2)   
n=6
print(A(n))
