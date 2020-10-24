def eh_crescente (lista): 
    if lista == []: 
		return True
	i = 1
	x = lista[0]
	while i < len(lista): 
		if lista[i] > x:
			x = lista[i]
		else:
			return False
		i += 1
	return True 
