def eh_crescente(lista):
    i = 0
    while i < len(lista):
        if i + 1 > i:
            i = i + 1
        elif i + 1 < i:
            return False
    return True