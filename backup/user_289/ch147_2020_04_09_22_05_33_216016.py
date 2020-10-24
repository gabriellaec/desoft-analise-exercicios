def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if not i in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    valor = 0
    for value in dicionario.values():
        if value > valor:
            valor = value
    return valor