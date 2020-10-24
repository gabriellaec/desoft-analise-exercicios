def estritamente_crescente(lista):
    lista_crescente = []
    lista_crescente.append(lista[0])
    for i in lista:
        if lista[i] > lista[i + 1]:
            lista_crescente.append(lista[i])
    return lista_crescente