def primeiras_ocorrencias(stri):
    dici1={}
    lista=[]
    lista2=[]
    for e in stri:
        lista.append(e)
    for i in range(0,len(stri)):
        lista2.append(i)
    for n,m in zip(lista,lista2):
        if n not in dici1.keys():
            dici1[n]=m
    return dici1