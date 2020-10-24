def eh_crescente(lista):
    for i in range(len(lista)):
        if lista[i+1]>lista[i]:
            return True
        else:
            return False