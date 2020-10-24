def conta_ocorrencias(lista):
    dicionario = {}
    for i in range(0,len(lista)):
        dicionario[lista[i]] = lista.count(lista[i])
    return dicionario
def mais_frequente(lista2):
    x = conta_ocorrencias(lista2)
    b = max(x.values())
    for u in x.keys():
        if x[u] == b:
            return u