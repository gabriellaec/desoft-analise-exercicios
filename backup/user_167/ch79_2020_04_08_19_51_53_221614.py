def monta_dicionario (l1,l2):
    d={}
    for e in l1:
        for i in l2:
            d[e]=[i]
    return d 