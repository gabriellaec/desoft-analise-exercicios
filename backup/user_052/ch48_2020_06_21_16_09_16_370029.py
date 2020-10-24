def eh_crescente (lista):
    crescente = False
    for i in range(len(lista)-1):
        if lista[i+1] <= lista[i]:
            crescente = False
        else:
            crescente = True
    return crescente
        