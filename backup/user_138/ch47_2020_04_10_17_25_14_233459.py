def estritamente_crescente(lista):
    i=0
    listaB=[]
    listaB=lista[0]
    a=0
    while i<len(lista):
        if len(lista)>0:
             listaB=lista[0]
            if lista[i+1]>listaB[a]:
                listaB.append(lista[i+1])
                a+=1
        i+=1
    return listaB