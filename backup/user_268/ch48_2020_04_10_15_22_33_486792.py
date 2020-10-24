def eh_crescente(lista):    
    a = len(lista)
    b = a - 1
    for i in range (b):
        if lista[i] >= lista[i + 1]:
            return False
        else:
            return True