def nome_usuario(string):
	contador = 0
	lista = []
	for i in string:
		if i == "@":
			pass
		else:
			contador += 1
	for i in string:
		if i != "@":
			lista.append(i)
        elif i == "@":
            break
	usuario = ("".join(lista))
	return usuario