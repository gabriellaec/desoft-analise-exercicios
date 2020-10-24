def estritamente_crescente(lista):
	if len(lista) == 0:
		return
	result = []
	result.append(lista[0])
	n = 0

	while n < (len(lista) - 1):
		print(lista)
		print(n)
		print(lista[n])
		if lista[n + 1] > result[n]:
			if lista[n + 1] > lista[n]: 
				result.append(lista[n + 1])
		print(result)
	n += 1
	return result