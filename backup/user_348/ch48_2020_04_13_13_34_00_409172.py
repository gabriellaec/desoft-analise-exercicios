def eh_crescente(lista):
    i = 1
    t = i - 1
    while i < len(lista):
        if lista[i] > lista[t]: 
            return True
        else:
            return False
        i = i + 1 