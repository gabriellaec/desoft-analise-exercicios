def eh_crescente(lista):
    i = 0
    crescente = True
    while crescente and i < len(lista):
        if lista[i + 1] > lista[i]:
            i += 1
        else:
            crescente = False
    return crescente