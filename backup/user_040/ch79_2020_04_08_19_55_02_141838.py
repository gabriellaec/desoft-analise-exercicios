def monta_dicionario(x,y):
    lista = []
    n = 0
    while n < len(x)-1:
        lista[n] = [x[n],y[n]]
        n += 1
    dicionario = {}
    for z in lista:
        dicionario[z[0]] = z[1]
    return dicionario