def lista_caracteres(string):
	letras = []
	for i in string:
		if i not in letras:
			letras.append(i)
	return letras 
