def apaga_repetidos(texto):
    saida = ''
    for i in range(len(texto)):
        if texto[i] not in saida:
            letra = texto[i]
            saida = saida + letra
        else:
            asterisco = '*'
            saida = saida + asterisco
    return saida
    