def calcula_fibonacci(x):
    i=2
    f=[1]*x
    f[0]=1
    f[1]=1
    while i<x:
        f[i]=f[i-1]+f[i-2]
        i+=1
    return f