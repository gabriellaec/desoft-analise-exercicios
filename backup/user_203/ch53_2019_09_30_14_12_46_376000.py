def inverte_lista (lista):
	if lista == []:
		return lista
	i = len(lista) - 1
	listaInvertida = []
	while i >= 0:
		listaInvertida.append(lista[i])
		i -= 1
	return listaInvertida
	
        
    