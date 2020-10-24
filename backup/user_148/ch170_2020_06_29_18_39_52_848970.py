def apaga_repetidos(frase):
    i = 0
    while i<len(frase):
        x = frase.count(frase[i])
        if x > 1:
            return frase.replace(frase[i], '*')
        i += 1