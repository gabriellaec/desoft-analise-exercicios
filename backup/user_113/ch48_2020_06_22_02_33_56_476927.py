def eh_crescente(lista):
    for i in range(0, len(lista)):
        if lista[i+1]>lista[i]:
            return True
        elif lista[i+1]<lista[i]:
            return False