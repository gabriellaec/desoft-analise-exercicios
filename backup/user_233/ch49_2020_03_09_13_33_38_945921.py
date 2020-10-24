def inverte_lista(lista):
    
    lista_nova = lista
    
    for i in range(len(lista)):
        lista_nova[-i - 1] = lista[i]
    
    return lista_nova
        