def monta_dicionario(L1,L2):
    dicionario={}
    l=len(L1)
    for i in range(l):
        dicionario[L1[i]]=L2[i]
    return dicionario