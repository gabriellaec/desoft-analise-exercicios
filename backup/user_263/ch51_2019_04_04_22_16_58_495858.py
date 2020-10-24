def estritamente_crescente(lista):
    cresc=[]
    if lista==[]:
        cresc=cresc
    else:
        cresc.append(lista[0])
    i=1
    maior=0
    while i<len(lista):
        if lista[i]>maior:
            crescente.append(lista[i])
            maior=lista[i]
        i+=1
    return crescente