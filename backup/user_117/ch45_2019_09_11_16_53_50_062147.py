z = []
def zera_negativos(lista):
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            z.append(0)
        z.append(lista[i])
	return z
         