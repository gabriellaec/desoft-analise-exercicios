def estritamente_crescente (lista): 
	if lista == []: 
		return lista 
	i = 0
	lista2 = [] 
	x = lista[0]
	lista2.append(x) 
	while i < len(lista): 
		if lista[i] > x:
            x = lista[i]
			lista2.append(x)
		i+=1 
	return lista2
