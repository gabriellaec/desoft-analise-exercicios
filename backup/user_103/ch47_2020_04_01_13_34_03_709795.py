def estritamente_crescente(lista):
    i=1
    lista1=[lista[0]]
    while i < len(lista):
        if lista[i]>lista[i-1]:
            lista1.append(lista[i])
            i+=1
        if lista[i]<lista[i-1]:
            i+=1
        if lista[i]==lista[i-1]:
            del lista[i]
    print (lista1)
   