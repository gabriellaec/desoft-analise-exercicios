def conta_letras(texto):
    dicionario = dict()
    for i in texto:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario
        