def apaga_repetidos(frase):
    lista_letras = []
    substitui = ""
    for letra in frase:
        if letra in lista_letras:
            substitue += "*"
        else:
            substitui += letra
            lista_letras.append(letra)
        return substitui