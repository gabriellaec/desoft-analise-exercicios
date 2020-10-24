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

def estritamente_crescente(lista):
    if len(lista) > 0:
        lista2 = [lista[0]]
        n = lista[0]
        for i in range (len(lista) - 1):
            if n < lista[i + 1]:
                n = lista[i + 1]
                lista2.append(lista[i + 1])
            i += 1
        return lista2
    else:
        return []