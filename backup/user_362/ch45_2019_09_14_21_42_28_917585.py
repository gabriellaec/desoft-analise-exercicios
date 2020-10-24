def zera_negativos(lista):
	contador=0
	while contador < len(lista):
		if lista[contador]<0:
			lista[contador]=0
		contador+=1
	return lista