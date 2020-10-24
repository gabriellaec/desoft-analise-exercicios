def eh_crescente(lista): 
    i = 0
    f = True
    while i <= len(lista):
        if lista[i] >= lista[i+1]:
            f = False
        i += 1
    return f       