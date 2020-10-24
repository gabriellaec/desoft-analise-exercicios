def apaga_repetidos(palavra):
    saida = ""
    for letra in palavra:
        if letra in saida:
            saida += *
        else:
            saida += letra
    return saida