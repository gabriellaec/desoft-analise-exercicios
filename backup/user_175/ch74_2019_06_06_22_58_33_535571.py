def acha_bigramas(x):
    lista = []
    for i in range(len(x)-1):
        bigrama = x[i] + x[i+1]
        lista.append(bigrama)
    return lista
def conta_bigramas(x):
    colecao = {}
    for i in acha_bigramas(x):
        if i in colecao:
            colecao[i] += 1
        else:
            colecao[i] = 1
    return colecao