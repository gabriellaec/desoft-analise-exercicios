def classifica_lista (lista):
    crescente = True
    decrescente = True
    if 2 > len(lista):
        return "nenhum"
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            decrescente = False
        elif lista[i+1] < lista[i]:
            crescente = False
    if crescente:
        return "crescente"
    elif decrescente:
        return "decrescente"
    else:
        return "nenhum"