def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    i = 1
    a = 0
    lista_c = []
    lista_c = [lista[0]]
    while i < len(lista):
        if lista[i] > lista_c[a]:
            lista_c.append(lista[i])
            a += 1
        i += 1
    lista_d = []
    lista_d = [lista[0]]
    e = 1
    b = 0
    while e < len(lista):
        if lista[e] < lista_d[b]:
            lista_d.append(lista[e])
            b += 1
        e += 1   
    if lista_d == lista:
        return 'decrescente'
    elif lista_c == lista:
        return 'crescente'
    else:
        return 'nenhum'