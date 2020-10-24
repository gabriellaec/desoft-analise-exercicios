def conta_bigramas (string):
    contagem = {}
    i = 0
    for bigrama in (string):
        if not bigrama in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] += 1
        i += 1
    return contagem