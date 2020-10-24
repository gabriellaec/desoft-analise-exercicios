def conta_ocorrencias(palavras):
    contagem={}
    for palavra in palavras:
        if not palavra in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem