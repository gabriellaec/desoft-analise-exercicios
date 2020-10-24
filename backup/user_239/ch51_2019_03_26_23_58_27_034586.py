def estritamente_crescente(lista):
    i=0
    s=0
    k=[]
    while i<len(lista):
        if lista[i]>=lista[i-1] and lista[i]!=s:
            s=lista[i]
            k.append(lista[i])
        i+=1
    return k