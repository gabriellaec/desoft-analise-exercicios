def apaga_repetidos(texto):
    string = str(texto)
    lista = []
    apagado = ''
    for caracter in string:
        if caracter in lista:
            apagado += '*'
        else:
            apagado += caracter
            lista.append(caracter)
    return apagado