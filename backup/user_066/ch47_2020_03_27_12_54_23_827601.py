def estritamente_crescente(lista):
    lista2 = []
    i = 1
    lista2.append(lista[0])
    while i < len(lista):
        if lista[i]>lista[i-1]:
            lista2.append(lista[i])
    return lista2