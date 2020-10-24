def bairro_mais_custoso(dicionario):
    dicionario2={}
    dicionario3={}
    for k in dicionario:
        for i in range(6,12):
            if not k in dicionario2:
                dicionario2[k] = dicionario[k][i]
            else:
                dicionario2[k] += dicionario[k][i]

    return dicionario2
    for a, b in dicionario2.items():
        dicionario3[a] = sum(b)
    for i,j in dicionario2.items():
        if j == max(dicionario3.values()):
            return i
        