def inverte_lista(lista):
    tamanho = len(lista)
    x = tamanho
    
    lista2 = [None]*tamanho
    
    for i in lista:
        x = x - 1
        lista2[tamanho] = i
    return lista2
        