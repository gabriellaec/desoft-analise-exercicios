def conta_bigramas (string):
    contagem = {}
    for bigrama in string:
        if not bigrama in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] += 1
    return contagem