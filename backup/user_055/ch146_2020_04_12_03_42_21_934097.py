def conta_ocorrencias(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra not in lista_palavras:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem
