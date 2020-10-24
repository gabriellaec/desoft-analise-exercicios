def lista_caracteres(string):
	lista = []
	for i in string:
		if i not in lista:
			lista.append(i)
		else:
			pass
	return lista 