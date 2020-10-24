def estritamente_crescente(lista):
	crescente = []
	maxim = 0
	for i in lista:
		if lista[i] > maxim:
			maxim = lista[i]
			crescente.append(maxim)
	return crescente