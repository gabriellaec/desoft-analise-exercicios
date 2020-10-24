def inverte_lista(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        lista2.append(lista[len(lista) - i - 1])
        i+=1
    return lista2