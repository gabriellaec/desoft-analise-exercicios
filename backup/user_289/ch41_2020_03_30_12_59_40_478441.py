def zera_negativos(lista):
	nova_lista = lista
	i = 0
    while i < len(lista) -1:
        if nova_lista[i] < 0:
		nova_lista[i]= 0
	i += 1
	return nova_lista