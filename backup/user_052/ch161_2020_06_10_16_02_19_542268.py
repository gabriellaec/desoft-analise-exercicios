def PiWallis (n):
    i = 3
    r = 2
    while r <= n:
        soma *= r/i
        r += 2
        soma *= r/i
        i += 2
    return 2 * soma
        