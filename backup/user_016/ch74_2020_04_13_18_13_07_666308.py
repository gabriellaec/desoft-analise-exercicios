def conta_bigramas(palavra):
    x = list(palavra)
    lista = []
    dicionario = {}
    for i in range(0,len(lista)-1):
        lista.append(x[i] + x[i+1])
    for u in range(len(lista)):
        if u not in dicionario.keys():
            dicionario[u] = 1
        else:
            dicionario[u] = +1
    return lista