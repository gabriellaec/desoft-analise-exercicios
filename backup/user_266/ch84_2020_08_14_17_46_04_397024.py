def inverte_dicionario(dicio):
    dicio2={}
    for k,v in dicio.items():
        if not v in dicio2.keys(): dicio2[v]=[k]
        else: dicio2[v].append(k)
    return dicio2