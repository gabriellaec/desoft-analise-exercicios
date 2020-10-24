def inverte_lista(lista):
    
    lista_original = lista
    
    for i in range(len(lista_original)):
        lista[-i - 1] = lista_original[i]
    
    return lista
        