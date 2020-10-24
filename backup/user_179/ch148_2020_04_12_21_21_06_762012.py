def conta_letras (string):
    i = 0
    dicionario = {}
    while i < len(string):
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[string[i]] = values
        else:
            dicionario[string[i]] = 1
        i = i + 1
    return dicionario