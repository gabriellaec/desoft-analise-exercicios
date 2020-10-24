def apaga_repetidos(frase):

    frase = list(frase)

    for char in frase:
        for i in range(frase.index(char) + 1, len(frase)):
            if char == frase[i]:
                frase[i] = '*'

    return ''.join(frase)