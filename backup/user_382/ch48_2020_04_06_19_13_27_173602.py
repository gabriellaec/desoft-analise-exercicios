def eh_crescente(lista):
    if lista == []:
        return True
    if len(lista) == 1:
        return True
    for i in range(len(lista)-1):
        if lista[i+1] <= lista[i]:
            return False
    return True
