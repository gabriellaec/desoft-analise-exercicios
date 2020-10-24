def monta_dicionario(l1, l2):
    dicionario={}
    for i in range(len(l1)):
        p=l1[i]
        j=l2[i]
        dicionario[p]=j
    return dicionario