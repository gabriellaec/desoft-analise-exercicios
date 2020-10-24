def estritamente_crescente(lista):
    lista_crescente=[]
    lista1=lista
    for i in range(len(lista)):
        if lista1[i]<lista1[i+1]:
            lista_crescente.append(lista[i])
        