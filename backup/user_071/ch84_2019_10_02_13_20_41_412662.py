def inverte_dicionario(d):
    dict2={}
    lista1=[]
    lista2=[]
    for k, v in d:
        lista1=[v]
        lista2=[k]
    i=0
    while i<len(lista1):
        dict2[lista1[i]]=lista2[i]
    return dict2

