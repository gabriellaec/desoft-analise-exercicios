def monta_dicionario (L1, L2):
    dicionario = {}
    i = 0
    for chave in L1:
        dicionario[chave] = L2[i]
        i+=1
    return dicionario