def estritamente_crescente(lista):
    if len(lista) == 0:
        return []
    lista2 = [lista[0]]
    i = 1
    n = lista[0]
    while i < len(lista):
        if n < lista [i]:
            lista2.append(lista[i])
            n = lista [i]
        i += 1
        
    return lista2