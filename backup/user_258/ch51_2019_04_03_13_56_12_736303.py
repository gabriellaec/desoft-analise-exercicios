def estritamente_crescente(lista):
    cresc=[]
    if lista==[]:
        cresc=cresc
    i=1
    u=0
    while i<len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u==i:
            cresc.append(lista[i])
        i+=1
    return cresc
