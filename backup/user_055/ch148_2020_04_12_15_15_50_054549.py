def conta_letras(palavra):
    contagem_letras = {}
    for letra in palavra:
        if letra not in contagem_letras:
            contagem_letras[letra] = 1
        else:
            contagem_letras[letra] += 1
    return contagem_letras