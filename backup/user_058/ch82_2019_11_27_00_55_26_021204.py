def primeiras_ocorrencias(string):
	dicionario = {}
	lugar = 0
	for i in string:
		if i not in dicionario.keys():
			dicionario[i] = lugar
			lugar += 1
		else:
			lugar += 1
	return dicionario
            
    