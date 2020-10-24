def inverte_dicionario(idades):
    dicn={}
    for n,i in idades.items():
        if i in dicn.keys():
            dicn[i]+=", {0}]".format(n)
        else:
            dicn[i]="[{0}".format(n)
    return dicn

