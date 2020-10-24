def conta_bigramas(texto):
    contagem = {}
    for bigramas in texto:
        if not bigrama in contagem:
            contagem[bigramas] = 1
        else:
            contagem[bigramas] +=1
    return contagem