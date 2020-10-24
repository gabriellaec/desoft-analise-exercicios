def calcula_fibonacci(n):
    f = [1]*n
    for i,numero in enumerate(f):
        if i>1:
            f[i]=f[i-1]+f[i-2]
    return f