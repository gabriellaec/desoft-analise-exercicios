def apaga_repetidos(palavra):
    lista = []
    letra = ""
    for i in range(len(palavra)):
        if palavra[i] not in lista:
            lista.append(palavra[i])
            letra += palavra[i]
        else:
            letra += "*"
    return letra