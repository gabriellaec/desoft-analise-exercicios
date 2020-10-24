def estritamente_crescente(lista):
    if len(lista) == 0:
        return lista
    lista2 = [lista[0]]
    
    for item in lista[1:]:
        if item > lista2[-1]:
            lista2.append(item)
    return lista2