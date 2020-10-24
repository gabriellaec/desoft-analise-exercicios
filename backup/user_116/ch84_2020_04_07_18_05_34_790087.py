def inverte_dicionario(dici):
    dicioo={}
    for n ,p in dici.items():
        if p not in dicioo:
            dicioo[p]=[]
        dicioo[p].append(n)
    return dicioo