def eh_crescente(lista):
    i = 1
    t = 0
    while i < len(lista) and t< (len(lista)-1):
        if lista[i] > lista[t]: 
            return True
        else:
            return False
        i = i + 1
        t = t + 1