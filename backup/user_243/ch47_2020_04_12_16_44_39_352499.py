def estritamente_crescente(lista):
    lista1=[]
    lista1.append(lista[0])
    i=1
    a=0
    while i<len(lista):
        if lista[i]>lista[a]:
            lista1.append(lista[i])
            a+=1
        i+=1
    return lista1
           
            