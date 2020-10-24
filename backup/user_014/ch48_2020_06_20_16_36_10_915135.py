def eh_crescente (lista):
    i = 1
    crescente = True
    while i < len(lista):
        if lista[i - 1] > lista[i]:
            crescente = True
        else:
            crescente = False
        if crescente:
            return True
        else:
            return False
        i += 1