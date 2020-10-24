def estritamente_crescente(lista):
    i = 0
    lista_nova = []
    while i < len(lista):
        if lista[i+1] > lista[i]:
            lista_nova.append(lista[i+1])
        i += 1
    return lista_nova