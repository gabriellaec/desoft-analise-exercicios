def apaga_repetidos(letras):
    dic = {}
    novas = ""
    for letra in letras:
        if letra in dic:
            novas += "*"
        else:
            novas += letra
            dic[letra]=letra
    return novas