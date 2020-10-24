def separa_trios(lista):
	lista1 = []
	for i in range(0,len(lista),3):
		lista1.append(lista[i:i+3])
	return lista1
