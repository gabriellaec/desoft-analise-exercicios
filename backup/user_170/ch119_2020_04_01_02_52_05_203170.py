def calcula_euler(x, n):
    i = 1
    e = 2
    euler_x = 1 + x
    if x >= 2:
        while i < n:
            nfat = e
            f = 1
            while f < e:
                nfat = nfat * f
                f += 1
            print(nfat)
            euler_x += (x**e)/(nfat)
            e += 1
            i += 1
    return euler_x

print(calcula_euler(2, 2))