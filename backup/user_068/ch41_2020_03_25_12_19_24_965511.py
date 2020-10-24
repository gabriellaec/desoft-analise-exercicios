a = [9, -7, 5, -3, 8]
def zera_negativos(a):
    i = 0
    while i < len(a):
        if a[i] >= 0:
            a[i] = a[i]
        else:
            a[i] = 0
        i += 1
    return zera_negativos