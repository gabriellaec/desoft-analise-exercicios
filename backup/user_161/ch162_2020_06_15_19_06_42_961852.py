def verifica_lista(valores):
    par = True
    impar = True
    for valor in valores:
        if valor%2 == 0:  # PAR
            impar = False
        else:
            par = False
    
    if par and not impar:
        return "par"
    if impar and not par:
        return "ímpar"
    return "misturado"