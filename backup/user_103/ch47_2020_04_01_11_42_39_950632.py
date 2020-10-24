def estritamente_crescente(lista):
    lista1=[lista[i]]
    i=0
    while lista[i]<lista[i+1]:
        lista1.append(lista[i+1])
        i+=1
    print (lista1)
   