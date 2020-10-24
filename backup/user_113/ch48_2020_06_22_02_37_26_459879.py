def eh_crescente(lista):
    for i in lista:
        if lista[i+1]>lista[i]:
            return True
        elif lista[i+1]<lista[i]:
            return False