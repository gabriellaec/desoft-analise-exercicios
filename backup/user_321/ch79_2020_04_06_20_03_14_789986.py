def monta_dicionario(l1, l2):
    i = 0
    dicionario = {}
    for i in range(len(l1)):
        dicionario[l1[i]] = l2[i]
    return dicionario