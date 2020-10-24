def eh_crescente(lista):
    a = len(lista)
    if a==0:
        return False
    elif a == 1:
        return True
    else:
        for i in range (a-1):
            if lista[i] < lista[i+1]:
                return True
            else:
                return False