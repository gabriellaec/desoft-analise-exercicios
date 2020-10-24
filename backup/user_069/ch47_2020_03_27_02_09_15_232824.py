def estritamente_crescente (lista):
    lista_crescente = []
    lista_crescente.append(lista[0])
    i = 0
    while i < (len(lista)-1):
        if lista[i+1] > lista[i]:
            lista_crescente.append(lista[i+1])
        i += 1
    return lista_crescente