def apaga_repetidos(letras):
    lista = []
    novas_letras = ""
    for letra in letras:
        if letra in lista:
            novas_letras += '*'
        else:
            novas_letras += letra
            lista.append(letra)            
    return novas_letras