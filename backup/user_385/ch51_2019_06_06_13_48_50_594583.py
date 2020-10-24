def estritamente_crescente(n):
    lista=[]
    lista0=[]
    b=0
    i=0
    a=1
    while b<len(n):
        
        if lista[i]<lista[a]:
            lista0.append(b)
        i+=1
        a+=1
        b+=1
    return lista0    