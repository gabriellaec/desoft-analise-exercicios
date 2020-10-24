def estritamente_crescente(lista):
    i = 0
    lista_crescente = []
    while i < len(lista):
        if lista[i] > lista[i + 1]:
            lista_crescente.append(lista[i])
        i += 1
    return lista_crescente