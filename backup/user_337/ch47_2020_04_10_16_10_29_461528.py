def estritamente_crescente(lista):
    lista_cresce = []
    lista_cresce = [lista[0]]
    i = 1
    a = 0
    while i < len (lista):
        if lista[i] > lista_cresce[a]:
            lista_cresce.append(lista[i])
            a += 1
        i += 1
    return lista_cresce
        