def junta_listas(lista):
    result = []
    for item in lista:
        if (isinstance(item, (list, tuple))):
            result = lista.extend(item)
        else:
            result.append(item)
    return result
    