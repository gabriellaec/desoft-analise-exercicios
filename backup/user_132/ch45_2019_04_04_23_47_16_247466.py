def zera_negativos(n):
    i = 0
    for k in n:
        if n[i] < 0:
            n[i] = 0
        i = i + 1
    return n