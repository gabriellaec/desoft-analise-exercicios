def PiWallis (n):
    a = 1
    i = 0
    num = 2
    dem = 1
    while i < n:
        a *= num/dem
        if i % 2 == 0:
            den += 2
        else:
            num += 2
        i += 1
    return a * 2