def estritamente_crescente(lista):
    cresc=[lista[0]]
    i=1
    u=0
    while i<len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u==i:
            cresc.append(lista[i])
        i+=1
    return cresc