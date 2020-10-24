def conta_bigramas(palavra):
    bigrama = palavra[ : : 2]
    contagem = {}
    for bigrama in palavra:
        if not bigrama in contagem:
            contagem[bigrama]=1
        else:
            contagem[bigrama] += 1
    return contagem

