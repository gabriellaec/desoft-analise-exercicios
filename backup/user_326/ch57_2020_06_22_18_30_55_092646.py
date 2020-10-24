def verifica_progressao(lista):
    Qa = lista[1] - lista[0]
    Qg = lista[1] / lista[0]
    for i in range(len(lista)):
        fga = lista[0] + (i)*Qa
        fgg = lista[0] * Qg**(i)
        if fga == lista[i] and fgg == lista[i]:
            return 'AG'
        elif fga == lista[i] and fgg != lista[i]:
            return 'PA'
        elif fga != lista[i] and fgg == lista[i]:
            return 'PG'
        else:
            return 'NA'