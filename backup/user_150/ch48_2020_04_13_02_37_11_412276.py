def eh_crescente(lista):
    for i in range(0, len(lista)-1):
        if lista[i+1] > lista[i]:
            return True
        else:
            return False