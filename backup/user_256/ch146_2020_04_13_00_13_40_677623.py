def conta_ocorrencias(palavras):
    contagem = {}
    for elementos in palavras:
        if not elementos in contagem:
            contagem[elementos] = 1
        else:
            contagem[elementos]+=1
    return contagem