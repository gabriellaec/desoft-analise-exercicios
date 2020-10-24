def inverte_lista(lista):
    if len(lista) == 0:
        return lista
    else:
        l_invertida = []
    	i = len(lista) - 1
    	while i > 0:
        	l_invertida.append(lista[i])
        	i -= 1
    return l_invertida