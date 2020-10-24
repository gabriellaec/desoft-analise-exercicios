def eh_crescente(lista):
    i = 1
    t = 0
    while i < len(lista):
        if lista[i] > lista[t]: 
            t = t + 1
            return True
            
        else:
            return False
        i = i + 1