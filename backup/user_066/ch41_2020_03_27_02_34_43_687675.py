def zera_negativos(lista):
	k = 0
	for i in lista:
		while k < len(lista):
			if i < 0:
				lista[k]= 0
            k +=1
	return lista