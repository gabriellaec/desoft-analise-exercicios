def calcula_fibonacci(n):
    i=2
    f=[1]*n
    f[0]=1
    f[1]=1
    while i<n:
        f[i]=f[i-1]+f[i-2]
        i+=1
    return f