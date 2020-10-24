def conta_bigramas(palavra):
    bigrama = palavra[ : : 2]
    contagem = {}
    for bigrama in texto:
        if not bigrama in contagem:
            contagem[bigrama]=1
        else:
            contagem[bigrama] += 1
    return contagem

