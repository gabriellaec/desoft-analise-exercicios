def apaga_repetidos(letras):
    lista_letras= []
    substitui = ""
    for letra in letras:
        if letra in lista_letras:
            substitui += '*'
        else:
            substitui += letra
            lista_letras.append(letra)
    return substitui