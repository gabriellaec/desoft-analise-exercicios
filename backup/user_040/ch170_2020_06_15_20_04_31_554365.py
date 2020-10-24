def apaga_repetidos(palavra):
    saida = ""
    for letra in palavra:
        if letra in saida:
            saida.append("*")
        else:
            saida.append(letra)