def inverte_lista(lista):
	listainvertida = []
	index = len(srt(lista))
	while index > 0:
		listainvertida += lista[index - 1]
		index = index - 1
	return listainvertida