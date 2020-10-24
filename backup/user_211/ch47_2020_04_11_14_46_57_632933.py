def estritamente_crescente(lista):
    lista2=[]
    lista2[0]=lista[0]
    i=0
    while(i<len(lista)):
        if lista[i+1]>lista[0]:
            lista2.append(lista[i+1])
    return lista2