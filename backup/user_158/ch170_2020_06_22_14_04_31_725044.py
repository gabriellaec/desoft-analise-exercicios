def apaga_repetidos(texto):
    texto2 = ''
    for i in texto:
        if i not in texto2:
            texto2 += i
        else:
            texto2 += '*'
    return texto2