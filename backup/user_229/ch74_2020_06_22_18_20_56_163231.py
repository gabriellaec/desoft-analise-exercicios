def conta_bigramas(string):
    bigrama_qtd = {}
    for i in range(len(string) - 1):
        bi = '{0}{1}'.format(string[i], string[i+1])
        if bi in bigrama_qtd:
            bigrama_qtd[bi] += 1
        else:
            bigrama_qtd[bi] = 1
    return bigrama_qtd