def estritamente_crescente(lista):
    listax = []
    i = 0
    while i < len(lista):
        i += 1
        if lista[i] < lista[i+1]:
            listax.append(lista)
    return listax