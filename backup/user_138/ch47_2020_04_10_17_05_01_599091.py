def estritamente_crescente(lista):
    i=0
    listaB=[]
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista.append(listaB)
        i+=1
    return listaB