def conta_bigramas (string):
    contagem = {}
    for i in string:
        bigrama = string[i] + string[i+1]
        if not bigrama in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] += 1
    return contagem