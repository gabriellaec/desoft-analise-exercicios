def remove_vogais(string):
	vogais = ['a','e','i','o','u']
	letras = []
	for i in string:
		letras.append(i)
	c = 0 
	while c < len(string):
		for t in letras:
			if t in vogais:
				letras.remove(t)
			c += 1 

	return ''.join(letras)
