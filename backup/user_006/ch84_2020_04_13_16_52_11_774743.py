def inverte_dicionario(d1):
    d2={}
    for i in d1.values():
        for g in d1:
            if g==i:
                d2[i]=g
    return d2