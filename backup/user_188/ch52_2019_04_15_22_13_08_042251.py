def eh_crescente(lista):
    maximo = 0
    for i in lista:
        if i > maximo:
            maximo = i
        else:
            return False
    return True