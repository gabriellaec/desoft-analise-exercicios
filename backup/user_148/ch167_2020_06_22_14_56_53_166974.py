def bairro_mais_custoso(dicionario):
    dicionario2 = {}
    for k in dicionario:
        for v in range(6, 12):
            if not k in dicionario2:
                dicionario2[k] = dicionario[k][v]
            else:
                dicionario2[k] += dicionario[k][v]

    for k2 in dicionario2:
        for v2 in range(6, 12):
            s = sum(v2)
            if k2 == max(s):
                return k2
        