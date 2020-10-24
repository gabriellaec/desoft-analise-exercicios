def conta_bigramas(texto):
    contagem = {}
    bigrama = [i] + [i+1]
    for bigrama in texto:
        if not bigrama in contagem:
            contagem[bigrama] = 1
        else:
            contagem[bigrama] +=1
    return contagem