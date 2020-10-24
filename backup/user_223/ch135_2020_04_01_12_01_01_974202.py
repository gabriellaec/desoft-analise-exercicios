def equaliza_imagem(lista_pixel, k):
	i = 0
	lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	if lista_pixel[i]*k > 255:
		lista_nova[i] == 255
	i += 1
	return (lista_nova)