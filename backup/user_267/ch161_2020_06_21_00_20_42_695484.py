def PiWallis(n):
    serie = 1
    a = 2
    b = 1
    i = 0
    while i < n:
        if i%2 != 0:
            b += 2
        else:
            a += 2
        serie *= (a/b)
        i += 1
    pi = serie*2
    return pi