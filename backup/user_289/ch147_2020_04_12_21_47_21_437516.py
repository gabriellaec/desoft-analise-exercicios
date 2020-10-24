def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    return max(dicionario, key=dicionario.get)

