def apaga_repetidos(texto):
    string = str(texto)
    lista = []
    for caracter in string:
        if caracter not in lista:
            lista.append(caracter)
        else:
            apagado = string.replace(caracter, '*')
            string = apagado
    return string