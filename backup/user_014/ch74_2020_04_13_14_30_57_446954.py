def conta_bigramas (string):
    contagem = {}
    for letra1,letra2 in string:
        if not letra1,letra2 in contagem:
            contagem[letra1,letra2] = 1
        else:
            contagem[letra1,letra2] += 1
    return contagem