def eh_crescente(lista):
    i = len(lista) - 1
    while i > 0:
        if lista[i] > lista[i-1]: 
            return True
        else:
            return False
        i = i - 1 