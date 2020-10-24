def equaliza_imagem(lista_pixel, k):
	i = 0
	lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	if lista_nova[i]*k > 255:
		lista_nova[i] == 255
	else:
		lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	i += 1
	return (lista_nova)