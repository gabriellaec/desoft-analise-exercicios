def calcula_fibonacci(n):
    f = [1,1]
    i = 0
    while(i < n):
        p = f[i + 1] + f[i]
        f.append(p)
        i += 1
    return f
        