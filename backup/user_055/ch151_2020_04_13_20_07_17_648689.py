def eh_crescente(lista_crescente):
    if lista_crescente == [] or len(lista_crescente) == 1:
        return True
    for i in range(len(lista_crescente) - 1):
        if lista_crescente[i] >= lista_crescente[i + 1]:
            return False
    return True

def eh_decrescente(lista_decrescente):
    if lista_decrescente == [] or len(lista_decrescente) == 1:
        return True
    for i in range(len(lista_decrescente) - 1):
        if lista_decrescente[i] <= lista_decrescente[i + 1]:
            return False
    return True

def classifica_lista(lista_numeros):
    if eh_crescente == True:
        return 'crescente'
    if eh_decrescente == True:
        return 'decrescente'
    else:
        return 'nenhum'