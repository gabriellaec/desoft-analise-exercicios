def calcula_fibonacci(n):
    i=2
    f=[1]*n
    while i<n:
        f[i]=f[i-1]+f[i-2]
        i+=1
    return f