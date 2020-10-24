def monta_dicionario(lista,lista2):
	dic = {}
	for i in range(0, len(lista)):
		dic[lista[i]] = lista2[i]
	return dic