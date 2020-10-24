def monta_dicionario(x,y):
    lista = []
    n = 0
    while n < len(x):
        lista[n] = [x[n],y[n]]
    dicionario = {}
    for z in lista:
        dicionario[z[0]] = z[1]
    return dicionario