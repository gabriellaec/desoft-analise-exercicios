def conta_letras(palavra):
    dicionario = {}
    for letra in palavra:
        if letra not in dicionario:
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
    return dicionario
