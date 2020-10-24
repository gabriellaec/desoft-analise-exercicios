def eh_crescente(lista):
    i = 0
    maior = 0
    Verdade = 0
    while i < len(lista):
        if lista[i] > maior:
            Verdade = True
        else:
            Verdade = False
        i += 1
        
        return Verdade