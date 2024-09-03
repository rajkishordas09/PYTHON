def A(n):
    if n=='':
        return 0
    return int(n[-1])+A(n[:-1])*10   

n="1234"
print(A(n))
