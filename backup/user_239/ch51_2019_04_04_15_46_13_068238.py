def estritamente_crescente(lista):
    i=1
    k=[]
    s=lista[0]
    k.append(lista[0])
    if len(lista)>0:
        while i<len(lista):
            if lista[i]>=s and lista[i]!=s:
                s=lista[i]
                k.append(lista[i])
            i+=1
    else:
        k=[]
    return k