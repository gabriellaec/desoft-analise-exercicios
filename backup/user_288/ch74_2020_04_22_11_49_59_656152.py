def conta_bigramas (string):
    contagem = {}
    for bigrama in string:
        i= 0
        if not bigrama[i, i+1] in contagem:
            contagem[string] =1
        else:
            contagem[string] += 1
        i += 1    
    return contagem