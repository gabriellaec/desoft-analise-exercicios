def faixa_notas(lista):
    lista_nova = [0] * 3
    m = 0
    j = 0
    k = 0
    for i in range(len(lista)):
        if lista[i] < 5:
            m += 1
        elif lista[i] >=5 and lista[i] <= 7:
            j += 1
        else:
            k += 1
    lista_nova[0] = m
    lista_nova[1] = j
    lista_nova[2] = k
    return lista_nova
    
        