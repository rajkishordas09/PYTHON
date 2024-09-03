def a(m,n):
    for i in range(2,m+1):
        if (m%i==0)and(n%i==0):
            return False
        else:
            return True
print(a(6,12))