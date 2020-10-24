def zera_negativos (x):
    for i in x:
        if i < 0:
            i = 0
        else:
            i = i
    return x