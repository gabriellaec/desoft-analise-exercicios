def calcula_fibonacci(n):
    if n == 1:
        f = [1]
    else:
        f = [1,1]
    for i in range(2, n):
        f.append(f[i-1]+f[i-2])
    return f