def zera_negativos(x):
    i = len(x)
    j = 0
    while j < i:
        if x[j] < 0:
            x[j] = 0
        j += 1