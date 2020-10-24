def estritamente_crescente(lista):
    lista_nova = [lista[0]]
    for i in range(len(lista)):
        if lista[i] > lista[i-1] and lista[i] not in lista_nova:
            lista_nova.append(lista[i])
    return lista_nova


