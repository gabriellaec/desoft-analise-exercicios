def apaga_repetidos(texto):
    lista = []
    resposta = ''
    for i in range(len(texto)):
        if texto[i] not in lista:
            lista.append(texto[i])
            resposta += texto[i]
        else:
            resposta += '*'
    return resposta