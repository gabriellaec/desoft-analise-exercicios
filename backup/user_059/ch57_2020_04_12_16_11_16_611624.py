def verifica_progressao(lista):
    E = 0
    if l[1]-l[0] == l[2]-l[1]:
        E = 'PA'
    elif l[1]/l[0] == l[2]/l[1]:
        E = 'PG'
    else:
        E = 'NA'
    return E