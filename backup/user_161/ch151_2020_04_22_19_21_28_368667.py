def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"

    crescente = True
    decrescente = True

    for l in range(1, len(lista)):
        if lista[l] >= lista[l-1]:
            decrescente = False
        if lista[l] <= lista[l-1]:
            crescente = False

    if crescente:
        return "crescente"
    if decrescente:
        return "decrescente"
    return "nenhum"