def monta_dicionario(x,y):
    dicionario = {}
    n = 0
    for z in x:
        dicionario[z] = y[n]
        n +=1
    return dicionario