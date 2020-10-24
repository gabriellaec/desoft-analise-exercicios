def primeiras_ocorrencias(palavra):
    contagem = {}
    x = 0
    for letra in palavra:
        if letra not in contagem:
            contagem[letra] = x
        x += 1
    return contagem