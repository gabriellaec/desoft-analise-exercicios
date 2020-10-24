def calcula_finonacci(n):
    f = [0]*n
    f[0] = f[1] = 1
    i = 2
    while i<n:
        f[i] = f[i-1] + f[i-2]
        i += 1
    return f
