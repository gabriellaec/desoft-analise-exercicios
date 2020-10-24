def estritamente_crescente(lista):
    i=1
    lista1=[lista[0]]
    while lista[i]<lista[i+1]:
        lista1.append(lista[i+1])
        i+=1
    if lista[i]>lista[i+1]:
        i+=1
    print (lista1)
   