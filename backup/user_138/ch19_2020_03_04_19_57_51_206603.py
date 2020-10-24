def classifica_triangulo (x,y,z):
    if x=y and x=z and y=z:
        classificacao="equilátero"
	elif x=y and x=z and y!=z:
        classificacao="isóceles"
	else:
        classificacao="escaleno"
	return classificacao