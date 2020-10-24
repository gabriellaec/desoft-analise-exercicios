def PiWallis(n):
    pi = 2
    for i in range(1,n):
        f1 = (2 * i)/(2 * i - 1)
        f2 = (2 * i)/(2 * i + 1)
        pi = pi * f1 * f2
    return pi