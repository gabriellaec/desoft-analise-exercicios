def conta_bigramas(string):
    lista = []
    for i in range(len(string)-1):
        lista.append(string[i] + string[i+1])
    dicionario = {}
    for bigrama in lista:
        n = lista.count(bigrama)
        dicionario[bigrama] = n
    return dicionario