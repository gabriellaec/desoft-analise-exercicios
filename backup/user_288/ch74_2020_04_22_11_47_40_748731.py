def conta_bigramas (string):
    contagem = {}
    for bigrama in string:
        if not bigrama in contagem:
            contagem[string] =1
        else:
            contagem[string] += 1
    return contagem