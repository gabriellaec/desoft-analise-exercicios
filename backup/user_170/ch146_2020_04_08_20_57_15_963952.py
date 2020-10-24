def conta_ocorrencias(palavras):
    contagem = {}
    for word in palavras:
        if not word in contagem:
            contagem[word] = 1
        else:
            contagem[word] +=1
    return contagem