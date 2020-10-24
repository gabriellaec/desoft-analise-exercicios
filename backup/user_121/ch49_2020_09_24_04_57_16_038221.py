def inverte_lista(lista):
    i=1
    lista_nova=[]
    while i<len(lista):
        lista_nova.append(lista[-i])
        i+=1
    lista_nova.append(lista[0])
    return lista_nova