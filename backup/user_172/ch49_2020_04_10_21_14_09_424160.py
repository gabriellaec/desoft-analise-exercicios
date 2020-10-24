def inverte_lista(lista):
    lista_inv = []
    i = 1
    while i < len(lista)/2:
        lista_inv.append(lista[-i])
        i+=1
    return lista_inv