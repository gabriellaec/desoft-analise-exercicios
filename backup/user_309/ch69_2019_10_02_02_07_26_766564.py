def junta_lista(lista):
    resultado = []
    for i in lista:
        if (isinstance(i, (list, tuple))):
            resultado = lista.extend(i)
        else:
            resultado.append(i)
    return resultado