def apaga_repetidos(texto):
    x = ''
    for i in texto:
        if i in x:
            x += '*'
        else:
            x += i
    return x