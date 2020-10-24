def estritamente_crescente(lista):
    i=0
    listaB=[]
    listaB=lista[0]
    while i<len(lista):
        if lista[i+1]>listaB[i]:
            listaB.append(lista[i+1])
        i+=1
    return listaB