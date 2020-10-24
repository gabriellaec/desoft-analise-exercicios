def primeiras_ocorrencias(a):
    dicionario = {}
    lista = []
    for i in range(len(a)-1):
        lista.append(a[i])
        
    for i in lista:
        if i in a:
            dicionario[i] = i
    return dicionario