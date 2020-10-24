def estritamente_crescente(lista):
    cresc=[lista[0]]
    if lista[1]>lista[0]:
        cresc.append(lista[1])
    i=2
    u=i-(i-1)
    while i<len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u==i:
            cresc.append(lista[i])
        i+=1
    return cresc