def eh_crescente(lista):
    crescente=True
    for e in range(len(lista)-1):
        if lista[e]<=lista[e-1]:
            crescente=False
    return crescente