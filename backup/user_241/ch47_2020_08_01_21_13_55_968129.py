def estritamente_crescente(lista):
    listax = []
    listax.append(lista[0])
    i = 1
    while i < len(lista):
        if lista[i] > listax[-1] :
            listax.append(lista[i])
        i += 1
    return listax