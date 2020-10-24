def inverte_dicionario(idades):
    dicn={}
    for n,i in idades.items():
        if i in dicn.keys():
            dicn[i]+=n
        else:
            dicn[i]=n
    return dicn