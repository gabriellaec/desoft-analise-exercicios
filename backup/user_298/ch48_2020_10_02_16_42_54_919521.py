def eh_crescente(lista):
    t = 0
    while t < (len(lista)-1):
        if lista[t] >= lista[t+1]:
            return False
        t += 1
    return True