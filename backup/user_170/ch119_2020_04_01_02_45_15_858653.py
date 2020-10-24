def calcula_euler(x, n):
    i = 0
    e = 2
    euler_x = 1 + x
    while i < n:
        nfat = e
        f = 1
        while f <= e:
            nfat = nfat * f
            f += 1
        euler_x = (x**e)/(nfat)
        e += 1
        i += 1
    return euler_x

print(calcula_euler(2, 2))