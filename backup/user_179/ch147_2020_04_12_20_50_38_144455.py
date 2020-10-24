def mais_frequente (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[lista[i]] = values
        else:
            dicionario[lista[i]] = 1
        i = i + 1
    frequente = max(dicionario)
    return frequente

