def eh_crescente(lista):
    i = 0
    while i != len(lista):
        if i+1 > i:
            i += 1
            return True
        else:
            return False