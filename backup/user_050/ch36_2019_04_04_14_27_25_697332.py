def eh_primo (x):
    if x<2:
        return False
    contador = 2
    while contador<x:
        if x % contador == 0:
            return False
        contador +=1
	return True