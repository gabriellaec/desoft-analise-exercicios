def eh_crescente (lista):
    for i in range (0,len(lista)):
        if lista[i]>lista[i+1]:
            return False
        else:
            return True
        