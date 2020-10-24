def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    crescente = True
    decrescente = True
    for i in range(len(lista))-1:
        if lista[i+1]-lista[i] > 0:
            decrescente = False
        elif lista[i+1]-lista[i] < 0:
            crescente = False
    if crescente == True:
        return 'crescente'
    elif decrescente == True:
        return 'decrescente'
    else:
        return 'nenhum'
