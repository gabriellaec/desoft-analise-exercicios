def conta_bigramas(palavra):
    i = 0
    dicionario = {}
    while i < len(palavra):
        corte = palavra[i:i+2]
        if corte not in dicionario:
            dicionario[corte] = 1
        else:
            dicionario[corte] += 1
        i += 1
    return dicionario