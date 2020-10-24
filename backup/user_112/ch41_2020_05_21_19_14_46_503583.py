def zera_negativos(n):
    x = len(n)
    i = 0
    while i < x:
        if n[i] < 0:
            n[i] == 0
            i += 1
        else:
            i += 1
    return n