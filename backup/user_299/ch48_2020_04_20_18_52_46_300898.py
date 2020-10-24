def eh_crescente(lista):
    crescente = True
    for i,e in enumerate(lista):
        if i+1 > len(lista):
            d=1
        elif i+1 < len(lista):
            d = lista[i+1] - lista[i]
        if d <= 0:
            crescente = False
    return crescente
    