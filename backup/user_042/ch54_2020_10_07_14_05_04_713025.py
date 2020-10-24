def calcula_fibonacci(n):
    f[0]*n
    if n == 0:
        return[]
    if n == 1:
        return [1]
    f[0] = 1
    f[1] = 1
    i = 2
    while i < len(f):
        f[i] = f[i-1]+f[i-2]
        i += 1
        return f
        