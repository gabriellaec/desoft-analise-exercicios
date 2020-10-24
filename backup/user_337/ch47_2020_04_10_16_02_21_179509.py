def estritamente_crescente(lista):
    lista_cresce = []
    lista_cresce = [lista[0]]
    i = 1
    while i < len (lista):
        if lista[i] > lista_cresce[i-1]:
            lista_cresce.append(lista[i])
        i += 1
    return lista_cresce
        