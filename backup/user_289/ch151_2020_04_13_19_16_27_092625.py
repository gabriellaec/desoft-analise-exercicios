def eh_crescente(lista): 
    i = 1
    L = len(lista)
    while i < L:
        if lista[i-1] < lista[i]:
            i += 1
        else:
            return False
    return True

def eh_decrescente(lista): 
    e = 1
    L2 = len(lista)
    while e < L2:
        if lista[e-1] > lista[e]:
            e += 1
        else:
            return False
    return True

def classifica_lista(lista_numeros):
    if eh_crescente(lista_numeros) == True:
        return 'crescente'
    elif eh_decrescente(lista_numeros) == True:
        return 'decrescente'
    else:
        return 'nenhum'
    
    
    
    