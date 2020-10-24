def estritamente_crescente(lista):
    i=0
    listaB=[]
    listaB=lista[0]
    a=0
    while i<len(lista):
        if lista[i+1]>listaB[a]:
            listaB.append(lista[i+1])
            a=i
        i+=1
    return listaB