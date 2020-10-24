def acha_bigramas(string):
	lista = []
	for i in range(len(string)-1):
		bigrama = string[i:i+2]
		if bigrama not in lista:
			lista.append(bigrama)
		else:
			pass
	return lista 
