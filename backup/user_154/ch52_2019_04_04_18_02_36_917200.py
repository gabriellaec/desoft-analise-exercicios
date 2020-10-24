def eh_crescente(lista):
    start = 0
    
    for x in lista:
        if x > start:
            start = x
        else:
            return False
    return True