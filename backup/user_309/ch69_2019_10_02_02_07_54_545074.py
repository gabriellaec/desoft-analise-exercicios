def junta_listas(lista):
    resultado = []
    for i in lista:
        if (isinstance(i, (list, tuple))):
            resultado = lista.extend(i)
        else:
            resultado.append(lista)
    return resultado