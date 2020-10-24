def inverte_lista(lista):
    
    lista_original = list(lista)
    
    for i in range(len(lista)):
        lista[-i-1] = lista_original[i]
    
    return lista