f = []
def calcula_fibonacci(n):
    f[0] = 1
    f[1] = 1
    i = 2
    while i <= n:
        fe = f[i-1]+f[i-2]
        f.append(fe)
    i += 1
    return lista
    