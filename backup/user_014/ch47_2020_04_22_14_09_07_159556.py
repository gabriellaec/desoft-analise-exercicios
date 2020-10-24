def estritamente_crescente (lista):
    i = 0
    lista_nova = [lista[0]]
    while i < len(lista):
        if lista[i] > lista_nova[len(lista_nova) -1]:
            lista_nova.append(lista[i])
        i += 1
    return lista_nova