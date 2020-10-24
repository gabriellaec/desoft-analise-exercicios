def zera_negativos(lista):
	nova_lista = lista
	i = 0
    while i < len(lista):
        if lista[i] < 0:
		    nova_lista.append(0)
	        i += 1
        else:
            nova_lista.append(lista[i])
	return nova_lista