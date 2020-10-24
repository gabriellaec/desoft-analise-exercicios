def zera_negativos(inteiros):
    for i in range(len(inteiros)):
        if inteiros[i] < 0:
            inteiros[i] = 0
    return inteiros
     