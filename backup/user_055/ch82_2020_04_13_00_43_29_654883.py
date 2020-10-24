def primeiras_ocorrencias(palavra):
    contagem = {}
    for letra in palavra:
        if letra not in contagem:
            contagem[palavra] = letra
    return contagem