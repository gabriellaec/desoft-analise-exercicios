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
    y=conta_ocorrencias(p)
    for i in y.values():
        lista.append(i)
        a=0
        while a<len(lista):
            b=0
            c=1
            while b<len(lista):
                if lista[a]>lista[b]:
                    b+=1
                    c+=1
                else:
                    b=len(lista)
            if c==len(lista):
                x=y[a]
                return x
            else:
                a+=1
                
            
        
        
        
        
        
            
        