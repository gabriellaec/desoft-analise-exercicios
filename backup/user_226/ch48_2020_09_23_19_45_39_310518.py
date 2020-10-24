def eh_crescente(lista):
    i = 1
    crescente = True
    while crescente and i < len(lista):
        if lista[i] > lista[i - 1]:
            i += 1
        else:
            crescente = False
    return crescente