def eh_crescente(lista):
    
    i = 1
    
    Verdade = True
    
    while i < len(lista) and Verdade:
        if lista[i] > lista[i-1]:
            i += 1
        else:
            Verdade = False
    return Verdade