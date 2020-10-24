def  estritamente_crescente(lista):
    lista1=[0]*len(lista)
    i=0
    lista1[0]=lista[0]
    while i<len(lista):
        if lista[i+1]>lista1[i]:
            lista1[i+1]=lista[i+1]
            
        i+=1
    return lista1