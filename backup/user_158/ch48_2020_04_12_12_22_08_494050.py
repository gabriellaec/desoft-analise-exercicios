def eh_crescente(lista):
    i=0
    while i < len(lista):
        if (lista[i+1] - lista[i]) < 0:
            return False
        i +=1
    return True