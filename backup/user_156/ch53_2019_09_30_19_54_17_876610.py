def inverte_lista(lista):
    tamanho = len(lista)
    x = tamanho
    for i in lista:
        x = x - 1
        lista[len(lista)] = i
    return lista
        