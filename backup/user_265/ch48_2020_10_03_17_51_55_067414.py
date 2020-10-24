def eh_crescente(lista):
    i = 0
    if len(lista) == 0:
        return True
    if len(lista) == 1:
        return True
    while i < len(lista):
        if lista[i] < lista[i+1]:
            i += 1
            if len(lista) == i:
                break
        elif lista[i] == lista[i+1]:
            i += 1
            return False
        else:
            return False