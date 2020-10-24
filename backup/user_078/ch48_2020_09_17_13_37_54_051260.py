def eh_crescente(lista):
    i1 = 0
    i2 = 1
    while i2 < len(lista):
        if lista[i2] > lista[i1]:
            i1 += 1
            i2 += 1            
        else:
            return False

    return True
