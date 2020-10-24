def equaliza_imagem(lista_pixel, k):
	i = 0
	lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	if lista_pixel[i]*k > 255:
		lisa_pixel[i] == 255
	else:
		lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	i += 1
	return (lista_nova)