def eh_crescente(lista):
    if lista == []:
        return False
    for i in range(len(lista)-1):
        if lista[i+1] <= lista[i]:
            return False
    return True

