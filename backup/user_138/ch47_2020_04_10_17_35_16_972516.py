def estritamente_crescente(lista):
    listaB=[]
    i=1
    a=0
    if len(lista)>0:
        listaB=lista[0]
    while i<len(lista):
        if lista[i]>listaB[a]:
            listaB.append(lista[i])
            a+=1
        i+=1
    return listaB