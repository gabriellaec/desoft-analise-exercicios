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
    lista=[]
    lista1=[]
    y=conta_ocorrencias(p)
    for i, v in conta_ocorrencias(p).items:
        lista.append(i)
        lista.append(v)
    k=0
    while k<len(lista):
        c=0
        for b in range (len(lista)):
            if lista1[k]>lista1[b]:
                c+=1
            else:
                c=len(lista)+2
        if c==len(lista)-1:
            return lista[k]
        else:
            k+=1
                
            
        
            
                
            
        
        
        
        
        
            
        