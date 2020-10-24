def inverte_lista(lista):
    lista_invert = []
    for e in lista:
        lista_invert.append(lista[(-e)])
    return(lista_invert)