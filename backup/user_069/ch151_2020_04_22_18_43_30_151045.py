def classifica_lista (lista):
    if len(lista) < 2:
        return 'nenhum'

    lista_c = []
    lista_c.append(lista[0])
    lista_d = []
    lista_d.append(lista[0])
    c = lista[0]
    d = lista[0]

    for i in range(len(lista)):
        if lista[i] > c:
            c = lista[i]
            lista_c.append(c)

        elif lista[i] < d:
            d = lista[i]
            lista_d.append(d)

    if lista == lista_c:
        return 'crescente'

    elif lista == lista_d: 
        return 'decrescente'

    else:
        return 'nenhum'