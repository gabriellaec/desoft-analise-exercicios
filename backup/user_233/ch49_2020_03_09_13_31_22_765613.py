def inverte_lista(lista):
    
    lista_original = lista
    
    for i in range(len(lista_original)):
        lista[i] = lista_original[-i - 1]
        