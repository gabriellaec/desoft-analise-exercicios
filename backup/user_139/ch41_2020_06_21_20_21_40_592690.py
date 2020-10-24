def zera_negativos(x):
    i = 0
    while i < len(x):
        if x[i] < 0:
            x[i] = 0
            i +=1
        else:
            i +=1
    return x