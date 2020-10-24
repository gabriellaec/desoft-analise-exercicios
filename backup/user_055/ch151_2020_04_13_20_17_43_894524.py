def eh_crescente(lista_crescente):
    if len(lista_crescente) < 2:
        return False
    for i in range(len(lista_crescente) - 1):
        if lista_crescente[i] >= lista_crescente[i + 1]:
            return False
    return True
print(eh_crescente([1, 4]))

def eh_decrescente(lista_decrescente):
    if len(lista_decrescente) < 2:
        return False
    for i in range(len(lista_decrescente) - 1):
        if lista_decrescente[i] <= lista_decrescente[i + 1]:
            return False
    return True

def classifica_lista(lista_numeros):
    if eh_crescente(lista_numeros) == True:
        return 'crescente'
    if eh_decrescente(lista_numeros) == True:
        return 'decrescente'
    else:
        return 'nenhum'