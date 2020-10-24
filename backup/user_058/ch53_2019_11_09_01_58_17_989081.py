def inverte_lista(lista):
    listainvertida = []
    index = len(lista)
    while index > 0:
    	listainvertida += lista[index - 1]
        index -= 1
    return listainvertida