def estritamente_crescente(lista):
    cresc=[]
    if lista==[]:
        cresc=cresc
    else:
        cresc.append(lista[0])
    i=1
    u=0
    while i<len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u==1:
            cresc.append(lista[i])
        i+=1
    return cresc