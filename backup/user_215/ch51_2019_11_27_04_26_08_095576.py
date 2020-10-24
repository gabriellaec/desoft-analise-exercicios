def estritamente_crescente(lista):
    lista_nova = [lista[0]]
    for i in range(len(lista)):
        if lista[i] > lista[i-1]:
            lista_nova.append(lista[i])
    return lista_nova


