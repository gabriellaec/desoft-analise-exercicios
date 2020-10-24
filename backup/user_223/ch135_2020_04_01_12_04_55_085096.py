def equaliza_imagem(lista_pixel, k):
	l = len(lista_pixel)
	i = 0
	while i < l:
		if int(lista_pixel[i])*k>255:
			lisa_pixel[i] == 255
	    else:
		    lista_pixel[i]=int(lista_pixel[i])
		    lista_pixel[i]*=k
		    i += 1
	return (lista_pixel)