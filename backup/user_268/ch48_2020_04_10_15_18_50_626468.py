def eh_crescente(lista):
    a = len(lista)
    for i in range (a-1):
        if lista[i] < lista[i+1]:
            return True
        else:
            return False