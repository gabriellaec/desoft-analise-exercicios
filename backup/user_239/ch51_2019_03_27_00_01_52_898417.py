def estritamente_crescente(lista):
    i=0
    k=[]
    s=lista[0]
    k.append(lista[0])
    while i<len(lista):
        if lista[i]>=lista[i-1] and lista[i]!=s:
            s=lista[i]
            k.append(lista[i])
        i+=1
    return k