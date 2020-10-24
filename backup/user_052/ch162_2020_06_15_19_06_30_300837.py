def verifica_lista (valores):
    par = True
    impar = True
    for valor in valores:
        if valor % 2 == 0:   # par
            impar = False
        else:
            par = False

    if par and not impar:
        return "par"
    elif impar and not par:
        return "ímpar"
    return "misturado"

            