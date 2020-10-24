def acha_bigramas(string):
	lista = []
	for i in range(len(string)-2):
		lista.append(string[i:i+2])
	return lista 