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
        i+=1
    return dici
def mais_frequente(p):
    y=conta_ocorrencias(p)
    mais=0
    for i, v in y.items():
        if v>mais:
            j=i
            mais=v
    return j