def estritamente_crescente(lista):
    listax = []
    i = 0
    while i < len(lista):
        if lista[i] > listax[-1] :
            listax.append(lista[i])
        i += 1
    return listax