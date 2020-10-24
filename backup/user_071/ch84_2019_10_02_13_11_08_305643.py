def inverte_dicionario(d):
    dict2={}
    lista1=[]
    lista2=[]
    for i in d:
        lista1[i]=d.keys()
        lista2[i]=d.values()
    dict2[lista2[i]]=lista1[i]
    return dict2
