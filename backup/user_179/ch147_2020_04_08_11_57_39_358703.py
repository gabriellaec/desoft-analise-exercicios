def mais_frequente (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[lista[i]] = values
        else:
            dicionario[lista[i]] = 1
        if dicionario[i] > dicionario[i-1]:
            a = dicionario[i]
        else:
            a = dicionario[0]
        i = i + 1
    return 