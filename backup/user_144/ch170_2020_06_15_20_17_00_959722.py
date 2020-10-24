def apaga_repetidos(letras):
    dic = {}
    novas_letras = ""
    for letra in letras:
        if letra in dic:
            novas_letras += '*'
        else:
            novas_letras += letra
            dic[letra] = letra
            
    return novas_letras