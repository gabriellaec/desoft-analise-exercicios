def eh_crescente(lista):
    i = 0
    while i < len(lista):
        if i + 1 > i:
            return True
        i += 1
        else:
            return False