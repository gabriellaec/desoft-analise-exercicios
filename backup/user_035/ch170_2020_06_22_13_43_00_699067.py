def apaga_repetidos(texto):
    lista_repetidos = []
    for i in texto:
        if i in lista_repetidos:
            texto[i] = "*"
        else:
            lista_repetidos.append(texto[i])
    return texto