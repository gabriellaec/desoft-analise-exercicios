def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    i = 1
    a = 0
    lista_cresce = []
    lista_cresce = [lista[0]]
    while i < len(lista):
        if lista[i] > lista_cresce[a]:
            lista_cresce.append(lista[i])
            a += 1
        i += 1
    lista_decresce = []
    lista_decresce = [lista[0]]
    e = 1
    b = 0
    while e < len(lista):
        if lista[e] < lista_decresce[b]:
            lista_decresce.append(lista[e])
            b += 1
        e += 1   
    if lista_decresce == lista:
        return 'decrescente'
    elif lista_cresce == lista:
        return 'crescente'
    else:
        return 'nenhum'