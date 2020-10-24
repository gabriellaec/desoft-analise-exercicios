def calcula_fibonacci(n):
    f = []
    f.append(1)
    f.append(1)
    i=2
    while i < n:
        f[i] = f[i-1] + f[i-2]
        i+=1
    return f