def eh_crescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i + 1] > lista [i]:
            pass
        else:
            return False
        if i == len(lista)-2:
            return True
        i += 1