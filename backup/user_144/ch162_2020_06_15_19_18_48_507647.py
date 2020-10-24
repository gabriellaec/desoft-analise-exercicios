def verifica_lista(valores):
    par = True
    impar = False
    for valor in valores:
        if valor%2 == 0:
            impar = False
        else:
            par = False

    if par and not impar:
    	return "par"
    if impar and not par:
   		return "ímpar"