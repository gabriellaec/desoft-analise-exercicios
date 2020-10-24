def conta_bigramas(n):
    dicionario = {}
    lista = []
    for i in range(0,len(n)-1):
        lista.append(n[i]+n[i+1])
    for e in lista:
        if e in dicionario:
            dicionario[e] = dicionario[e] + 1
        else:
            dicionario[e] = 1
    return dicionario
