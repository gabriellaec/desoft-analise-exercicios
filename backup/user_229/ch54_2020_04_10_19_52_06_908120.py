def calcula_fibonacci(n):
    if n == 1:
        f = [1]
    else:
        f = [1,1]
    for i in range(2, n-1):
        f.append(f[i-2]+f[i-3])
    return f