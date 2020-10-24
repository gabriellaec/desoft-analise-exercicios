def conta_bigramas (palavra):
    i = 0
    lista = []
    dicionario = {}
    while i < (len(palavra)-2):
        lista.append(palavra[i]+palavra[i+1])
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[lista[i]] = values
        else:
            dicionario[lista[i]] = 1
        i = i + 1
    return dicionario