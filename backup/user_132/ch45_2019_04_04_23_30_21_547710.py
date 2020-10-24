def zera_negativos(n):
    for k in n:
        if n[k]<0:
            n[k] = 0
    return n