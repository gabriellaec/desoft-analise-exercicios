def nome_usuario(string):
	contador = 0
	lista = []
	for i in string:
		if i == "@":
			pass
		else:
			contador += 1
	for i in string:
		while i != "@":
			lista.append(i)
	usuario = ("".join(lista))
	return usuario