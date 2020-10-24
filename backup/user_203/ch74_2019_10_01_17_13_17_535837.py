def acha_bigramas (string): 
	bigramas = []
	i = 0 
	while i<len(sting)-1: 
		bigr = string[i]+string[i+1]
		bigramas.append(bigr)
		i+=1
	return bigramas 
def conta_bigramas(string): 
	bigramas = acha_bigramas(string)
	dicionario = {} 
	i = 0
	while i<len(bigramas):
		if bigramas[i] in dicionario:
			dicionario[bigramas[i]] = 1
			i+=1 
	return dicionario 
    