def eh_crescente(lista):
    i = 1
    t = 0
    while i < len(lista):
        if lista[i] > lista[t]: 
            return True
            t = t + 1
        else:
            return False
        i = i + 1