def estritamente_crescente(lista):
    for i in len(lista)-1:
        if lista[i] >= lista[i+1]:
            return False
    return True
def estritamente_decrescente(lista):
    for i in len(lista)-1:
        if lista[i] <= lista[i+1]:
            return False
    return True
def classifica_lista(lista):
    if estritamente_crescente(lista):
        return 'crescente'
    elif estritamente_decrescente(lista):
        return 'decrescente'
    else:
        return 'nenhum'