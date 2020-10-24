def PiWallis(n):
    num = 2
    den = 1
    i = 1
    meiopi = 2/1
    while i <= n:
        if i%2 == 0:
            num += 2
        if i%2 != 0:
            den += 2
        pi = pi*(num/den)
        i += 1
    pi = 2*meiopi
    return pi