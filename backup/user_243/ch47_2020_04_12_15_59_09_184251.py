def estritamente_crescente(lista):
    lista1=[]
    lista1[0]=lista[0]
    i=0
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista[i]=lista1[i]
            i+=1
    return lista1
           
            