def eh_crescente(lista):
    i = 1
    while i < len(lista):
        if lista[i]>lista[i-1]:
            i += 1
        elif lista[i]<lista[i-1]:
            return False
    return True