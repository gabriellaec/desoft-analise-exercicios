def classifica_lista (lista):
    crescente = True
    decrescente = True
    nenhum = True
    if 2 > len(lista):
        return "nenhum"
    for i in lista:
        if lista[i] > lista[i-1]:
            decrescente = False
        elif lista[i] < lista[i-1]:
            crescente = False
    if crescente:
        return "crescente"
    elif decrescente:
        return "decrescente"
    else:
        return "nenhum"