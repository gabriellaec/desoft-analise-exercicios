def zera_negativos(n):
    l = len(n)
    x = 0
    while x < (l):
        if int(n[x]) < 0:
            n[x] = 0
            x = x + 1
        else:
            x = x + 1
    return n