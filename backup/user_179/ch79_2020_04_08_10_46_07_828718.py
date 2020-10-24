def monta_dicionario (l1,l2):
    dicionario = {}
    while i < len(l1):
        dicionario[l1[i]] = l2
        i += 1
    return dicionario