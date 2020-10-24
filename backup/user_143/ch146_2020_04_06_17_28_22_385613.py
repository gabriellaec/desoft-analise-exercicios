def conta_ocorrencias(l):
    dici={}
    for i in range(len(l)):
        a=0
        while l[i]==l[a]:
            a+=1
        dici[l[i]]=a
    return dici
        