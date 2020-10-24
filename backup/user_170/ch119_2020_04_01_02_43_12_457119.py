def calcula_euler(x, n):
    i = 0
    e = 2
    f = 1
    nfat = e
    euler_x = 1 + x
    while i < n:
        nfat = e
        while f <= e:
            nfat = nfat * f
            f += 1
        euler_x = (x**e)/(nfat)
        e += 1
        i += 1
    return euler_x
