
def eh_crescente(lista):
    if len(lista) > 0:
        ant = lista[0]
    else:
        return False
    for i in range(1, len(lista)):
        if lista[i] <= ant:
            return False
        ant = lista[i]
    return True