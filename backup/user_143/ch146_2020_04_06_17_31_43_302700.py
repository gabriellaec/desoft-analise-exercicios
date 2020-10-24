def conta_ocorrencias(l):
    dici={}
    i=0
    while i<len(l):
        a=0
        c=0
        while a<len(l):
            if l[i]==l[a]:
                a+=1
                c+=1
            else:
                a+=1
        dici[l[i]]=c
    return dici
        