def eh_crescente(lista):
    i = 0
    if lista[i+1]>lista[i]:
        i=i+1
        return True
    else:
        return False