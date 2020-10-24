def eh_pa(lista):

    pa = True
    razao_pa = lista[1] - lista[0]
    for numero in lista:
        if numero != lista[-1]:
            sub_teste = lista[lista.index(numero) + 1] - lista[lista.index(numero)]
            if sub_teste != razao_pa:
                pa = False
    
    if pa:
        return True
    else:
        return False

def eh_pg(lista):

    pg = True
    for numero in lista:
        soma = 0
        soma += numero
        if soma == 0:
            return True

        elif soma != 0 and numero == 0:
            return False
    
    razao_pg = lista[1] / lista[0]

    for numero in lista:
        if numero != lista[-1]:
            div_teste = lista[lista.index(numero) + 1] / lista[lista.index(numero)]
            if div_teste != razao_pg:
                pg = False

    if pg:
        return True
    else:
        return False

def verifica_progressao(lista):

    if eh_pa(lista) and eh_pg(lista):
        return 'AG'
    
    elif eh_pa(lista):
        return 'PA'
    
    elif eh_pg(lista):
        return 'PG'
    
    else:
        return 'NA'