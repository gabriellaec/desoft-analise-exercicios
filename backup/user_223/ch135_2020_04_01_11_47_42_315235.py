i = 0
def equaliza_imagem(lista_pixel, k):
	lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	if lista_nova[i]*k > 255:
		lisa_nova[i] == 255
	else:
		lista_nova = [lista_pixel[i]*k for (lista_pixel[i]) in lista_pixel]
	i += 1
	return (lista_nova)