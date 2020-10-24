def zera_negativos (lista):
	i = 0
	comprimento = len(lista)
	while i < comprimento:
		if lista[i] < 0:
			lista[i] = 0
		i += 1
	return lista       
    