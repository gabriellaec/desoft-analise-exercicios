def bairro_mais_custoso(dicionario):
    dicionario2 = {}
    for k in dicionario:
        for v in range(6, 12):
            if not k in dicionario2:
                dicionario2[k] = dicionario[k][v]
            else:
                dicionario2[k] += dicionario[k][v]

    for k2, v2 in dicionario2.items():
        v2max = 0
        if v2 > v2max:
            v2max = v2
    
    return k2
