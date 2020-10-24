def eh_aritmetica(lista):
    i = 0
    c = 0
    while i < len(lista) - 1:
        if lista[i] != lista[i+1]:
            if 2*lista[i] == lista[i-1] + lista[i+1]:
                c += 1
                if c == len(lista) - 2:
                    return 'PA'
        i = i + 1    
def eh_geometrica(lista):
    i = 0
    g = 0
    while i < len(lista) - 1:
        if lista[i] != lista[i+1]:
            if lista[i]**2 == (lista[i-1]*lista[i+1]):
                g += 1
                if g == len(lista) - 2:
                    return 'PG'
        i += 1
def geometrica_aritmetica(lista):
    i = 0
    pag = 0
    while i < len(lista)-1:
        if lista[i] == lista[i+1]:
            pag += 1
            if pag == len(lista) -1:
                return 'AG'
        i += 1
def verifica_progressao(lista):
    x = lista
    if eh_aritmetica(x):
        return 'PA'
    elif eh_geometrica(x):
        return 'PG'
    elif geometrica_aritmetica(x):
        return 'AG'
    else:
        return 'NA'