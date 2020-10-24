def eh_crescente(lista):
    crescente = True
    for i,e in enumerate(lista):
        d = lista[i+1] - lista[i]
        if d <= 0:
            crescente = False
    return crescente
    