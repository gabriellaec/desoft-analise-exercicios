def estritamente_crescente(lista):
    i=1
    s=0
    cresc=[]
    while i<len(lista):
        if lista[i]>lista[i-1]+1:
            cresc.append(lista[i])
        i+=1
    return cresc