def  estritamente_crescente(lista):
    lista1=[0]*len(lista)
    i=0
    while i<len(lista):
        if lista[i]>lista1[i-1]:
            lista1[i]=lista[i]
        i+=1
    return lista1