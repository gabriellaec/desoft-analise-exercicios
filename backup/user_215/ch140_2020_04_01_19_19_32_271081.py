def faixa_notas(lista):
    lista_nova: []
    m =
    j =
    k =
    for i in len(lista):
        if lista[i] < 5:
            m += 1
        elif lista[i] >=5 and lista[i] =< 7:
            j += 1
        elif lista[i] > 7:
            k += 1
    lista_nova.append(m)
    lista_nova.append(j)
    lista_nova.append(k)
    return lista_nova
    
        