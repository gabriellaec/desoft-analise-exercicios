def lista_unica(lista):
    junta_lista = []
    for i in lista:
        if (isinstance(i, (list, tuple))):
            junta_lista = lista.extend(i)
        else:
            junta_lista.append(i)
    return junta_lista