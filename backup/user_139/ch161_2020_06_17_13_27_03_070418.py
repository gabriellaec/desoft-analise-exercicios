def PiWallis (n):
    a = 1
    i = 0
    num = 2
    den = 1
    pi = a * 2
    while i < n:
        a *= num / den
        if i %2 == 0:
            num += 2
        else:
            den += 2
        i += 1
    return pi