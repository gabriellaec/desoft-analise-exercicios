def PiWallis(n):
    pi = 1
    for i in range(2, n+2):
        pi *= (i-1)/i if x % 2 == 0 else i/(i-1)
    return pi*2