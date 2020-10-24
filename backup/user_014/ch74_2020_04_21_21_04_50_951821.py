def conta_bigramas (string):
    contagem = {}
    for bigrama in (string, 2):
        if not  in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] += 1
    return contagem