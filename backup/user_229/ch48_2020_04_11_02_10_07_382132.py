def eh_crescente(lista):
    i = 1
    while i < len(lista) - 1:
        if lista[i] > lista[i-1]:
            i += 1
        else:
            return False
    return True