def verifica_progressao(lista):
    print(lista)
    pa = False
    pg = False
    Qa = 0
    Qg = 0
    Qa = lista[1] - lista[0]
    if lista[0] != 0: 
        Qg = lista[1] / lista[0]
    for i in range(len(lista)):
        fga = lista[0] + (i)*Qa
        fgg = lista[0] * Qg**(i)
        if fga == lista[i] and fgg == lista[i]:
            pa = True
            pg = True
        elif fga == lista[i] and fgg != lista[i]:
            pa = True
            pg = False
        elif fga != lista[i] and fgg == lista[i]:
            pa = False
            pg = True
    if pa and pg:
        return 'AG'
    elif pa and not pg:
        return 'PA'
    elif pg and not pa:
        return 'PG'
    else:
        return 'NA'