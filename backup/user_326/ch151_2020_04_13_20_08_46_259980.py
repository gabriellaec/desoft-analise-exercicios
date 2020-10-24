def classifica_lista(lista):
    numero_anterior = 0
    checa_resultado = 0
    checa_se_so_decresce = 0
    checa_se_so_cresce = 0
    if len(lista) == 1:
        return 'nenhum'
    for indice in range(len(lista)):
        if indice != 0:
            if lista[indice] > numero_anterior:
                numero_anterior = lista[indice]
                checa_se_so_cresce = 1
            elif lista[indice] < numero_anterior:
                numero_anterior = lista[indice]
                checa_se_so_decresce = 2
        else:
            numero_anterior = lista[indice]
    checa_resultado = checa_se_so_cresce + checa_se_so_decresce
    if checa_resultado == 1:
        return 'crescente'
    elif checa_resultado == 2:
        return 'decrescente'
    else:
        return 'nenhum'