def zera_negativos(x):
    for i in range(len(x)):
        if x[i]<0:
            x[i]=0
    return x