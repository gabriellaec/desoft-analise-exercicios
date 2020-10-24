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
    lista=[]
    for i in y.values():
        c=i
        lista.append(c)
    a=0
    while a<len(lista):
        b=0
        if lista[a]>lista[b]:
            b+=1
        else:
            a+=1
    b=lista[a]
    k=0
    while k<len(y):
        if y[k]==b:
            return y[k].keys()
        else:
            k+=1
        
        
        
        
        
            
        