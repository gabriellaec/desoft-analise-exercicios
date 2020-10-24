def estritamente_crescente(lista):
    cresc=[lista[0]]
    i=0
    u=i-(i-1)
    while i<len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u==i:
            cresc.append(lista[i])
        i+=1
    return cresc