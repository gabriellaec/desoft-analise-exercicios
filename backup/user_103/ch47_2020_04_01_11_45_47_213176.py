def estritamente_crescente(lista):
    i=0
    lista1=[lista[i]]
    while lista[i]<lista[i+1]:
        lista1.append(lista[i+1])
        i+=1
    if lista[i]>lista[i+1]:
        i+=1
    return lista1
   