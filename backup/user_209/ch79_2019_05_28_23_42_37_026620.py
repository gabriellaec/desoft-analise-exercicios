def monta_dicionario (l1,l2):
    dicionario = {}
    for e in range (len(l2)):
        dicionario[l1[e]] = l2[e]
    return dicionario