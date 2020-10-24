import numpy as np
def equaliza_imagem(lista_pixel, k):
	lista_array = np.array(lista_pixel)
	lista_nova = lista_array*k
	return (lista_nova)