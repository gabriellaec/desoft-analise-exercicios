def classifica_triangulo (x,y,z):
    if x=y=z:
        classificacao="equilátero"
	elif x=y!=z:
        classificacao="isóceles"
	else x!=y!=z:
        classificacao="escaleno"
	return classificacao