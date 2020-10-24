def estritamente_crescente(lista):
	new_lista = []
	new_lista.append(lista[0])
	i = 1
	max_valor = lista[0]
	while i < len(lista):
		if max_valor < lista[i]:
			new_lista.append(lista[i])
			max_valor = lista[i]
		i = i + 1
        
	return new_lista