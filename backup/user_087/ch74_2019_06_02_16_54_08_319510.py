def conta_bigramas(palavra):
    bigrama_qtd = dict()
    lista = []
    i = 0
    while i < len(palavra):
        lista.append(palavra[i:i+2])        
        if len(palavra[i:i+2]) == 1:
            lista.remove(palavra[i:i+2])
        i += 1
    for bigrama in lista:
        if bigrama in bigrama_qtd:
            bigrama_qtd[bigrama] += 1
        else:
            bigrama_qtd[bigrama] = 1
    return bigrama_qtd