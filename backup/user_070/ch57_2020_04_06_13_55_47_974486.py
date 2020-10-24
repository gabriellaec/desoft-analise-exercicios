def verifica_progressao(lista):
    x = 1
    y = 1
    pa = 0
    pg = 0
    d = lista[1] - lista[0]
    r = lista[1] / lista[0]
    for i in lista:
        if x < len(lista):
            if i + d == lista[x]:
                pa += 1
        x += 1
    for i in lista:
        if y < len(lista):
            if i * r == lista[y]:
                pg += 1
        y += 1
    if pa == len(lista)-1 and pg == len(lista)-1:
        return 'AG'
    elif pa == len(lista)-1:
        return 'PA'
    elif pg == len(lista)-1:
        return 'PG'
    else:
        return 'NA'