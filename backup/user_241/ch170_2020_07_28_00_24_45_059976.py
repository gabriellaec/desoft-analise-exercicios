def apaga_repetidos(texto):
    x = ''
    for caractere in texto:
        if caractere in x:
            x = x + '*'
        else:
            x = x + caractere
    return x
            