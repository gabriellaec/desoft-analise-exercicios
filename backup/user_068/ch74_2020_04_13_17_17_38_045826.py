def conta_bigramas(a):
    dicionario = {}
    lista = []
    i = 0
    while i < len(a):
        lista.append(a[i] + a[i+1])
        i+=1
    for t in lista:
        if t in dicionario:
            dicionario[t] += 1
        else:
            dicionario[t] = 1
    return dicionario












    