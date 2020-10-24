def crescente(lista):
    for n in range(1, len(lista)):
        if lista[n] <= lista[n-1]:
            return False
    return True

def decrescente(lista):
    for n in range(1, len(lista)):
        if lista[n] >= lista[n-1]:
            return False
    return True

def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'

    elif crescente(lista) == True:
        return 'crescente'

    elif decrescente(lista) == True:
        return 'decrescente'

    return 'nenhum'