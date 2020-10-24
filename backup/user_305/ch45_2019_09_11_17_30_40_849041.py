def zera_negativos(lista):
	i = 0
	lista2 = []
	while i < len(lista):
		if lista[i]>=0:
			lista2.append(lista[i])
		elif lista[i] < 0:
			lista2.append(0)
		i +=1
	return lista2
