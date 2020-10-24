def conta_letras (string):
    i = 0
    dicionario = {}
    while i < len(string):
        if string[i] in dicionario:
            values = string.count(string[i])
            dicionario[string[i]] = values
        else:
            dicionario[string[i]] = 1
        i = i + 1
    return dicionario