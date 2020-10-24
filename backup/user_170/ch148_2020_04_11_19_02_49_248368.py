def conta_bigramas(string):
    contagem = {}
    bigrama = []
    for i in range(len(string)-1):
        bigrama.append(string[i]+string[i+1])
    for b in bigrama:
        if not b in contagem:
            contagem[b] = 1
        else:
            contagem[b] +=1
    return contagem